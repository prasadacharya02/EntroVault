"""Tests for the automated incident email notification subsystem."""

import importlib.util
import json
import os
import smtplib
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import config
from notification.incidents import Incident, IncidentTracker, count_estate_files
from notification.email_notifier import (
    DETECTION_STAGE, RECOVERY_STAGE, EmailNotifier,
)
from storage.database import connect, init_db, notification_sent


def _incident(affected: int = 5, estate: int = 18, dry_run: bool = False,
              recovered: bool = True) -> Incident:
    incident = Incident("test:key", "/victim/a.txt",
                        dry_run=dry_run, estate_total=estate)
    incident.mark_recovery_started()
    for i in range(affected):
        incident.record_outcome(f"/victim/file{i}.txt",
                                "QUARANTINED+RESTORED" if recovered
                                else "QUARANTINED+RESTORE_FAILED")
    return incident


class IncidentTrackerTests(unittest.TestCase):
    def test_campaign_key_groups_files_into_one_incident(self):
        tracker = IncidentTracker()
        first = tracker.begin(
            {"event_id": "e1", "file_path": "/v/a.txt"},
            {"campaign_id": "campaign-99"},
        )
        second = tracker.begin(
            {"event_id": "e2", "file_path": "/v/b.txt"},
            {"campaign_id": "campaign-99"},
        )
        self.assertIs(first, second)
        self.assertEqual(first.affected_count, 0)
        first.add_affected("/v/a.txt", recovered=True, outcome="RESTORED")
        self.assertEqual(second.affected_count, 1)

    def test_distinct_campaigns_are_distinct_incidents(self):
        tracker = IncidentTracker()
        a = tracker.begin({"event_id": "e1"}, {"campaign_id": "c-1"})
        b = tracker.begin({"event_id": "e2"}, {"campaign_id": "c-2"})
        self.assertIsNot(a, b)

    def test_counts_reflect_recovery_outcomes(self):
        incident = _incident(affected=5, estate=18, recovered=False)
        incident.mark_recovery_complete()
        self.assertEqual(incident.affected_count, 5)
        self.assertEqual(incident.failed_count, 5)
        self.assertEqual(incident.recovered_count, 0)
        self.assertEqual(incident.unaffected_count, 18 - 5)
        self.assertEqual(incident.recovery_status, "partial")

    def test_complete_incident_is_marked_completed(self):
        incident = _incident(affected=3, estate=10)
        incident.mark_recovery_complete()
        self.assertEqual(incident.recovery_status, "completed")

    def test_estate_count_ignores_missing_directory(self):
        with mock.patch.object(config, "VICTIM_USER_FILES",
                               "/nonexistent/path/xyz"):
            self.assertEqual(count_estate_files(), 0)


class EmailContentTests(unittest.TestCase):
    def _notifier(self, **cfg):
        overrides = {
            "EMAIL_SENDER_ADDRESS": "entrovault@example.com",
            "EMAIL_SENDER_PASSWORD": "secret",
            "VICTIM_EMAIL": "victim@example.com",
            "VICTIM_PROFILE_PATH": "/nonexistent/profile.json",
        }
        overrides.update(cfg)
        stack = [mock.patch.object(config, key, value)
                 for key, value in overrides.items()]
        for patcher in stack:
            patcher.start()
            self.addCleanup(patcher.stop)
        return EmailNotifier()

    def test_detection_body_uses_live_counts(self):
        notifier = self._notifier()
        incident = _incident(affected=5, estate=18)
        msg = notifier.build_detection_email(incident)
        body = msg.get_content()
        self.assertIn("5 affected file(s)", body)
        self.assertIn("13 file(s) are safe", body)
        self.assertEqual(msg["Subject"],
                         "EntroVault Security Alert – File Recovery in Progress")
        self.assertIn("EntroVault Security System", msg["From"])
        self.assertEqual(msg["To"], "victim@example.com")

    def test_recovery_body_reports_completion(self):
        notifier = self._notifier()
        incident = _incident(affected=5, estate=18)
        incident.mark_recovery_complete()
        msg = notifier.build_recovery_email(incident)
        body = msg.get_content()
        self.assertIn("Recovery is now complete", body)
        self.assertIn("5 affected file(s)", body)
        self.assertIn("13 file(s) remain safe", body)
        self.assertEqual(msg["Subject"],
                         "EntroVault Security Alert – File Recovery Complete")

    def test_recovery_body_admits_partial_recovery(self):
        notifier = self._notifier()
        incident = _incident(affected=4, estate=18, recovered=False)
        incident.mark_recovery_complete()
        body = notifier.build_recovery_email(incident).get_content()
        self.assertIn("partially complete", body)
        self.assertIn("could not be automatically restored", body)

    def test_dry_run_body_is_explicit_about_simulation(self):
        notifier = self._notifier()
        incident = _incident(affected=2, estate=4, dry_run=True)
        body = notifier.build_detection_email(incident).get_content()
        self.assertIn("simulation (dry-run)", body)


class NotifierDedupTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db_path = os.path.join(self.tmp.name, "events.db")
        init_db(self.db_path).close()
        self.profile = os.path.join(self.tmp.name, "profile.json")
        self._patches = [
            mock.patch.object(config, "DB_PATH", self.db_path),
            mock.patch.object(config, "VICTIM_PROFILE_PATH", self.profile),
            mock.patch.object(config, "VICTIM_EMAIL", "victim@example.com"),
            mock.patch.object(config, "EMAIL_ENABLED", True),
            mock.patch.object(config, "EMAIL_SEND_DRY_RUN", True),
            mock.patch.object(config, "EMAIL_SENDER_ADDRESS", "sender@example.com"),
            mock.patch.object(config, "EMAIL_SENDER_PASSWORD", "secret"),
        ]
        for patcher in self._patches:
            patcher.start()
            self.addCleanup(patcher.stop)
        self.notifier = EmailNotifier()

    def test_dry_run_send_is_recorded_and_not_duplicated(self):
        incident = _incident()
        first = self.notifier.notify_detected(incident)
        self.assertTrue(first["sent"])
        self.assertEqual(first["status"], "dry_run")
        second = self.notifier.notify_detected(incident)
        self.assertFalse(second["sent"])
        self.assertEqual(second["status"], "duplicate")
        self.assertEqual(self.notifier.notify_recovered(incident)["sent"], True)
        # Completion is its own stage and is sent independently.
        self.assertFalse(self.notifier.notify_recovered(incident)["sent"])

    def test_notification_row_is_persisted(self):
        incident = _incident()
        self.notifier.notify_detected(incident)
        conn = connect(self.db_path)
        try:
            self.assertTrue(notification_sent(conn, incident.incident_id,
                                              DETECTION_STAGE))
            rows = conn.execute(
                "SELECT status FROM notifications WHERE incident_id=? "
                "AND stage=?", (incident.incident_id, DETECTION_STAGE)
            ).fetchall()
        finally:
            conn.close()
        self.assertEqual([r[0] for r in rows], ["dry_run"])

    def test_disabled_notifier_sends_nothing(self):
        with mock.patch.object(config, "EMAIL_ENABLED", False):
            result = self.notifier.notify_detected(_incident())
        self.assertFalse(result["sent"])
        self.assertEqual(result["status"], "disabled")

    def test_missing_credentials_skip_without_raising(self):
        with mock.patch.object(config, "EMAIL_SEND_DRY_RUN", False), \
             mock.patch.object(config, "EMAIL_SENDER_ADDRESS", ""), \
             mock.patch.object(config, "EMAIL_SENDER_PASSWORD", ""):
            result = self.notifier.notify_detected(_incident())
        self.assertFalse(result["sent"])
        self.assertEqual(result["status"], "skipped")

    def test_smtp_delivery_success(self):
        with mock.patch.object(config, "EMAIL_SEND_DRY_RUN", False), \
             mock.patch("smtplib.SMTP") as smtp:
            result = self.notifier.notify_detected(_incident())
        self.assertTrue(result["sent"])
        self.assertEqual(result["status"], "sent")
        smtp.return_value.__enter__.return_value.send_message.assert_called()

    def test_smtp_failure_is_contained(self):
        with mock.patch.object(config, "EMAIL_SEND_DRY_RUN", False), \
             mock.patch("smtplib.SMTP",
                        side_effect=smtplib.SMTPException("boom")):
            result = self.notifier.notify_detected(_incident())
        self.assertFalse(result["sent"])
        self.assertEqual(result["status"], "failed")


class VictimProfileApiTests(unittest.TestCase):
    def _load_victim_app(self, profile_path):
        spec = importlib.util.spec_from_file_location(
            "victim_app_email_test",
            os.path.join(config.BASE_DIR, "victim_server", "app.py"),
        )
        module = importlib.util.module_from_spec(spec)
        with mock.patch.object(config, "VICTIM_PROFILE_PATH", profile_path), \
             mock.patch.object(config, "VICTIM_EMAIL", "default@victim.corp"):
            spec.loader.exec_module(module)
        module.VICTIM_PROFILE_PATH = profile_path
        return module

    def test_profile_default_and_update(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = os.path.join(directory, "victim_profile.json")
            module = self._load_victim_app(profile)
            client = module.app.test_client()

            data = client.get("/api/profile").get_json()
            self.assertEqual(data["email"], "default@victim.corp")

            ok = client.post("/api/profile",
                             json={"email": "user@victim.corp",
                                   "name": "Victim User"})
            self.assertEqual(ok.status_code, 200)
            self.assertEqual(ok.get_json()["email"], "user@victim.corp")

            # The change is persisted to the shared profile file.
            with open(profile, encoding="utf-8") as handle:
                self.assertEqual(json.load(handle)["email"], "user@victim.corp")

            bad = client.post("/api/profile", json={"email": "not-an-email"})
            self.assertEqual(bad.status_code, 400)


class PipelineNotificationIntegrationTests(unittest.TestCase):
    """The pipeline must emit exactly one detection + one completion alert."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.db_path = os.path.join(self.tmp.name, "events.db")
        init_db(self.db_path).close()
        self._patches = [
            mock.patch.object(config, "DB_PATH", self.db_path),
            mock.patch.object(config, "EMAIL_ENABLED", True),
            mock.patch.object(config, "EMAIL_SEND_DRY_RUN", True),
            mock.patch.object(config, "VICTIM_EMAIL", "victim@example.com"),
            mock.patch.object(config, "VICTIM_PROFILE_PATH",
                              os.path.join(self.tmp.name, "profile.json")),
        ]
        for patcher in self._patches:
            patcher.start()
            self.addCleanup(patcher.stop)

    def _event(self, event_id: str, path: str) -> dict:
        return {
            "event_id": event_id,
            "timestamp": "2026-01-01T00:00:00",
            "event_type": "MODIFIED",
            "file_path": path,
            "original_path": None,
            "file_extension": ".txt",
            "file_size": 100,
            "file_hash": "a" * 64,
            "entropy_overall": 7.9,
            "entropy_delta": 2.5,
            "threat_score": 90.0,
            "process": {},
        }

    def test_detection_and_completion_sent_once_per_incident(self):
        from monitoring.pipeline_runner import PipelineRunner

        runner = PipelineRunner()
        notifier = mock.Mock()
        runner.notifier = notifier

        decision = {
            "action": config.ACTION_TERMINATE_QUARANTINE,
            "action_name": "TERMINATED+QUARANTINED",
            "campaign": True,
            "campaign_id": "campaign-42",
            "sweep_events": [{"file_path": "/victim/b.txt"}],
        }

        with mock.patch.object(runner.engine, "decide",
                               return_value=decision), \
             mock.patch("monitoring.pipeline_runner.execute_response",
                        return_value="QUARANTINED+RESTORED"), \
             mock.patch.object(runner, "_post_kill_verification"):
            runner._on_analyzed_event(self._event("e1", "/victim/a.txt"))

        self.assertEqual(notifier.notify.call_count, 2)
        stages = [call.args[1] for call in notifier.notify.call_args_list]
        self.assertEqual(stages, [DETECTION_STAGE, RECOVERY_STAGE])

        # The incident tracked both the trigger file and the sweep target.
        incidents = runner.incidents.all()
        self.assertEqual(len(incidents), 1)
        self.assertEqual(incidents[0].affected_count, 2)

    def test_second_campaign_event_does_not_duplicate_alerts(self):
        from monitoring.pipeline_runner import PipelineRunner

        runner = PipelineRunner()
        real = EmailNotifier()
        outcomes: list[tuple[str, str]] = []
        original_notify = real.notify

        def spy(incident, stage):
            result = original_notify(incident, stage)
            outcomes.append((stage, result["status"]))
            return result

        real.notify = spy
        runner.notifier = real

        decision = {
            "action": config.ACTION_TERMINATE_QUARANTINE,
            "action_name": "TERMINATED+QUARANTINED",
            "campaign": True,
            "campaign_id": "campaign-42",
            "sweep_events": [],
        }

        with mock.patch.object(runner.engine, "decide",
                               return_value=decision), \
             mock.patch("monitoring.pipeline_runner.execute_response",
                        return_value="QUARANTINED+RESTORED"), \
             mock.patch.object(runner, "_post_kill_verification"):
            runner._on_analyzed_event(self._event("e1", "/victim/a.txt"))
            runner._on_analyzed_event(self._event("e2", "/victim/b.txt"))

        # Same campaign -> same incident -> one detection + one completion,
        # and the repeat attempts are recognised as duplicates.
        self.assertEqual(
            outcomes,
            [("detected", "dry_run"), ("completed", "dry_run"),
             ("detected", "duplicate"), ("completed", "duplicate")],
        )
        self.assertEqual(len(runner.incidents.all()), 1)


if __name__ == "__main__":
    unittest.main()
