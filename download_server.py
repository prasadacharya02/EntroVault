import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
PDF_FILE  = os.path.join(DOCS_DIR, "ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.pdf")
DOCX_FILE = os.path.join(DOCS_DIR, "ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.docx")
MD_FILE   = os.path.join(DOCS_DIR, "ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.md")
HTML_FILE = os.path.join(DOCS_DIR, "ENTROVAULT_REPORT_VIEW_AND_DOWNLOAD.html")

class DownloadHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path in ("/", "/index.html", "/view", "/report"):
            if os.path.exists(HTML_FILE):
                with open(HTML_FILE, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            else:
                self.send_error(404, "HTML report not found")

        elif path in ("/download-docx", "/docx"):
            if os.path.exists(DOCX_FILE):
                with open(DOCX_FILE, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                self.send_header("Content-Disposition", 'attachment; filename="ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.docx"')
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_error(404, "Word document (.docx) not found")

        elif path in ("/download-pdf", "/pdf"):
            if os.path.exists(PDF_FILE):
                with open(PDF_FILE, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/pdf")
                self.send_header("Content-Disposition", 'attachment; filename="ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.pdf"')
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_error(404, "PDF not found")

        elif path == "/view-pdf":
            if os.path.exists(PDF_FILE):
                with open(PDF_FILE, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/pdf")
                self.send_header("Content-Disposition", 'inline; filename="ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.pdf"')
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_error(404, "PDF not found")

        elif path in ("/download-md", "/md"):
            if os.path.exists(MD_FILE):
                with open(MD_FILE, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/markdown; charset=utf-8")
                self.send_header("Content-Disposition", 'attachment; filename="ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.md"')
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_error(404, "Markdown not found")

        else:
            self.send_error(404, "Path not found")

    def log_message(self, format, *args):
        pass

def run():
    server = HTTPServer(("0.0.0.0", 8080), DownloadHandler)
    print("Download server running on http://0.0.0.0:8080 ...")
    server.serve_forever()

if __name__ == "__main__":
    run()
