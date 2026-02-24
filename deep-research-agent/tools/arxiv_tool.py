from phase0.arxiv_search import search_arxiv

def arxiv_search_tool(query: str):
    """ search arxiv for reserch paper based on a quary"""
    return search_arxiv(query,max_results=3)