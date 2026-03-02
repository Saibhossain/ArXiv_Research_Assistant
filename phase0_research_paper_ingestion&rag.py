import arxiv

def search_arxiv(query, max_results=3):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "pdf_url": result.pdf_url,
            "summary": result.summary
        })
    return papers

# test arxiv_search
results = search_arxiv("retrieval augmented generation")
for p in results:
    print(p["title"])


# phase0/pdf_loader.py

import pdfplumber
import requests
from pathlib import Path

def download_pdf(url, save_path):
    r = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(r.content)

def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

Path("data/papers").mkdir(parents=True, exist_ok=True)

# phase0/chunker.py
def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks



# phase0/embed_store.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.texts = []

    def add_texts(self, chunks):
        embeddings = self.model.encode(chunks)
        self.texts.extend(chunks)

        if self.index is None:
            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(np.array(embeddings))

    def search(self, query, k=5):
        q_emb = self.model.encode([query])
        D, I = self.index.search(np.array(q_emb), k)
        return [self.texts[i] for i in I[0]]

# phase0/rag_qa.py

def answer_question(question, store):
    retrieved_chunks = store.search(question)
    context = "\n".join(retrieved_chunks)

    print("\n--- Retrieved Context ---\n")
    print(context[:1500])

store = VectorStore()
store.add_texts(["RAG combines retrieval and generation for grounded LLMs."])

answer_question("What is RAG?", store)