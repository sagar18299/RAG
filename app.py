from src.rag.search import RAGSearch

# Example usage
if __name__ == "__main__":
    rag_search = RAGSearch()
    query = "How would you design a real-time chat application in Node.js?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)