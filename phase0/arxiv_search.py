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


if __name__ == "__main__":
    results = search_arxiv("RAG  retrieval augmented generation")
    for p in results:
        print(p["title"])
