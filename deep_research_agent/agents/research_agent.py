from ..tools.arxiv_tool import arxiv_search_tool
from ..tools.pdf_tool import load_pdf_tool
from ..tools.retriever_tool import ingest_text_tool, retrieve_tool
from ..llm.local_llm import fake_llm

class ResearchAgent:
    def __init__(self):
        self.memory = []

    def run(self, user_query: str):
        print(f"\nUSER QUERY: {user_query}\n")

        # Step 1 — Thought
        thought = "I should search for relevant research papers."
        print("Thought:", thought)

        # Step 2 — Action
        papers = arxiv_search_tool(user_query)
        print("\nAction: arxiv_search_tool")
        print("Observation:", [p["title"] for p in papers])

        # Step 3 — Pick first paper
        pdf_url = papers[0]["pdf_url"]

        print("\nThought: I should read the most relevant paper.")

        text = load_pdf_tool(pdf_url)
        print("\nAction: load_pdf_tool")
        print("Observation: PDF text loaded")

        print("\nThought: I should store this knowledge.")

        result = ingest_text_tool(text)
        print("\nAction: ingest_text_tool")
        print("Observation:", result)

        print("\nThought: I can now answer the user's question.")

        retrieved = retrieve_tool(user_query)
        print("\nAction: retrieve_tool")
        print("\n--- Retrieved Context ---\n")
        for c in retrieved:
            print(c[:300])
            print("-" * 40)
