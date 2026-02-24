def fake_llm(prompt: str):
    """
    Temporary rule-based LLM for learning agent logic.
    Replace with real LLM later.
    """

    if "search" in prompt.lower():
        return "Action: arxiv_search"
    if "pdf" in prompt.lower():
        return "Action: load_pdf"
    if "explain" in prompt.lower():
        return "Action: retrieve"

    return "Action: finish"
