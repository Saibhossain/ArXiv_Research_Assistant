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
