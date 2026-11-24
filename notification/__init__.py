"""EntroVault incident notification subsystem.

When the detection pipeline confirms a ransomware-like incident it
opens an :class:`~notification.incidents.Incident`, tracks which files
were affected and how recovery went, and asks the
:class:`~notification.email_notifier.EmailNotifier` to alert the victim.
"""

from notification.incidents import Incident, IncidentTracker
from notification.email_notifier import EmailNotifier

__all__ = ["Incident", "IncidentTracker", "EmailNotifier"]
