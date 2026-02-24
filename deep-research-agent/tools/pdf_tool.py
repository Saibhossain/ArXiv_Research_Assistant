from phase0.pdf_loader import download_pdf, extract_text
from pathlib import Path

def load_pdf_tool(pdf_url: str):
    """
    Download and extract text from a PDF.
    """
    Path("data/papers").mkdir(exist_ok=True)

    pdf_path = "data/papers/temp.pdf"
    download_pdf(pdf_url, pdf_path)
    text = extract_text(pdf_path)

    return text[:8000]  # safety limit
