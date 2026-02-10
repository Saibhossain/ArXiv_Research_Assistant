from embed_store import VectorStore

def answer_question(question, store):
    retrieved_chunks = store.search(question)
    context = "\n".join(retrieved_chunks)

    print("\n--- Retrieved Context ---\n")
    print(context[:1500])


if __name__ == "__main__":
    store = VectorStore()
    store.add_texts(["RAG combines retrieval and generation for grounded LLMs."])

    answer_question("What is RAG?", store)
