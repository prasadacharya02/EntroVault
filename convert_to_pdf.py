# convert_to_pdf.py
"""
Converts docs/ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.md to a publication-grade,
beautifully styled, formal IEEE / University Dissertation PDF using markdown and xhtml2pdf,
with full Unicode / DejaVu font embedding.
"""

import os
import sys
import markdown
from xhtml2pdf import pisa

def md_to_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, "docs", "ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.md")
    pdf_path = os.path.join(base_dir, "docs", "ENTROVAULT_IEEE_PROJECT_REPORT_100_PAGES.pdf")

    if not os.path.exists(md_path):
        print(f"Error: {md_path} does not exist.")
        sys.exit(1)

    print(f"Reading markdown file: {md_path}")
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    print("Converting Markdown to HTML with tables, code fences, and formatting extensions...")
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"]
    )

    # Academic IEEE Dissertation CSS Styling with DejaVu font embedding
    custom_css = """
    @font-face {
        font-family: 'DejaVuSerif';
        src: url('fonts/DejaVuSerif.ttf');
    }
    @font-face {
        font-family: 'DejaVuSerif';
        src: url('fonts/DejaVuSerif-Bold.ttf');
        font-weight: bold;
    }
    @font-face {
        font-family: 'DejaVuSans';
        src: url('fonts/DejaVuSans.ttf');
    }
    @font-face {
        font-family: 'DejaVuSans';
        src: url('fonts/DejaVuSans-Bold.ttf');
        font-weight: bold;
    }
    @font-face {
        font-family: 'DejaVuSansMono';
        src: url('fonts/DejaVuSansMono.ttf');
    }
    @font-face {
        font-family: 'DejaVuSansMono';
        src: url('fonts/DejaVuSansMono-Bold.ttf');
        font-weight: bold;
    }

    @page {
        size: a4 portrait;
        margin: 2cm 2cm 2.5cm 2cm;
        @top-right {
            content: "EntroVault: Proactive Ransomware Defence";
            font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
            font-size: 8pt;
            color: #555555;
            font-style: italic;
        }
        @bottom-right {
            content: "Page " counter(page);
            font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
            font-size: 8pt;
            color: #555555;
        }
        @bottom-left {
            content: "IEEE Major Project Dissertation (200 Marks)";
            font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
            font-size: 8pt;
            color: #555555;
        }
    }

    body {
        font-family: 'DejaVuSerif', "Times New Roman", Times, serif;
        font-size: 10pt;
        line-height: 1.45;
        color: #111111;
        text-align: justify;
    }

    h1 {
        font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
        font-size: 16pt;
        font-weight: bold;
        color: #0b2545;
        text-align: center;
        margin-top: 22pt;
        margin-bottom: 14pt;
        page-break-before: always;
        text-transform: uppercase;
        border-bottom: 1.5pt solid #0b2545;
        padding-bottom: 5pt;
    }

    h2 {
        font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
        font-size: 12.5pt;
        font-weight: bold;
        color: #133c55;
        margin-top: 16pt;
        margin-bottom: 7pt;
        border-bottom: 0.5pt solid #cccccc;
        padding-bottom: 2pt;
    }

    h3 {
        font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
        font-size: 10.5pt;
        font-weight: bold;
        color: #1d4e89;
        margin-top: 11pt;
        margin-bottom: 5pt;
    }

    h4 {
        font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
        font-size: 9.5pt;
        font-weight: bold;
        color: #333333;
        margin-top: 8pt;
        margin-bottom: 4pt;
    }

    p {
        margin-top: 0pt;
        margin-bottom: 7pt;
        text-indent: 0pt;
    }

    hr {
        border: 0;
        height: 0.5pt;
        background-color: #bbbbbb;
        margin: 12pt 0;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 8pt;
        margin-bottom: 12pt;
        font-size: 8pt;
        font-family: 'DejaVuSans', Helvetica, Arial, sans-serif;
    }

    th {
        background-color: #0b2545;
        color: #ffffff;
        font-weight: bold;
        padding: 4.5pt 5pt;
        border: 0.5pt solid #0b2545;
        text-align: left;
    }

    td {
        padding: 4pt 5pt;
        border: 0.5pt solid #dddddd;
        vertical-align: top;
    }

    tr:nth-child(even) td {
        background-color: #f7f9fb;
    }

    pre, code {
        font-family: 'DejaVuSansMono', "Courier New", Courier, monospace;
        font-size: 7.5pt;
    }

    pre {
        background-color: #f4f6f8;
        border: 0.5pt solid #d0d7de;
        padding: 6pt;
        margin-top: 6pt;
        margin-bottom: 10pt;
        line-height: 1.25;
        white-space: pre-wrap;
    }

    code {
        background-color: #f0f2f5;
        padding: 1pt 2.5pt;
        border-radius: 2pt;
        color: #8b1e1e;
    }

    blockquote {
        margin: 6pt 0 10pt 12pt;
        padding: 4pt 8pt;
        border-left: 2.5pt solid #133c55;
        background-color: #f4f8fa;
        font-style: italic;
        color: #333333;
    }

    ul, ol {
        margin-top: 0pt;
        margin-bottom: 7pt;
        padding-left: 18pt;
    }

    li {
        margin-bottom: 2.5pt;
    }
    """

    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>EntroVault IEEE Major Project Dissertation</title>
    <style>
    {custom_css}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""

    print(f"Compiling publication PDF: {pdf_path} ...")
    with open(pdf_path, "wb") as pdf_file:
        pisa_status = pisa.CreatePDF(full_html, dest=pdf_file)

    if pisa_status.err:
        print(f"Error during PDF generation: {pisa_status.err}")
        sys.exit(1)

    pdf_size_bytes = os.path.getsize(pdf_path)
    pdf_size_mb = pdf_size_bytes / (1024 * 1024)
    print(f"PDF Successfully Generated!")
    print(f"Output File: {pdf_path}")
    print(f"File Size:   {pdf_size_mb:.2f} MB ({pdf_size_bytes:,} bytes)")

if __name__ == "__main__":
    md_to_pdf()
