from phase0.embed_store import VectorStore
from phase0.chunker import chunk_text

store = VectorStore()

def ingest_text_tool(text: str):
    """
    Chunk and store document text into vector memory.
    """
    chunks = chunk_text(text)
    store.add_texts(chunks)
    return f"Stored {len(chunks)} chunks."

def retrieve_tool(query: str):
    """
    Retrieve relevant document chunks for a question.
    """
    return store.search(query)
