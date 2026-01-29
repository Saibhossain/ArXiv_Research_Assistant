import pdfplumber
import requests
from pathlib import Path

def download_pdf(url,save_path):
    r = requests.get(url)
    with open(save_path,"wb") as f:
        f.write(r.content)

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

if __name__=="__main__":
    Path("data/papers").mkdir(parents=True,exist_ok=True)


