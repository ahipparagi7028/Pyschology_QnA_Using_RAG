# scripts/run_ingest.py
from pathlib import Path
from src.rag.data_loader import load_pdf
from src.rag.chunking import chunk_documents
from src.rag.embeddings import build_or_load_index

if __name__ == "__main__":
    pdf_path = Path("data/book.pdf")
    index_dir = Path("artifacts/index")
    embedding_model = "sentence-transformers/all-MiniLM-L6-v2"

    docs = load_pdf(pdf_path)
    chunks = chunk_documents(docs, chunk_size=1000, chunk_overlap=200)
    build_or_load_index(chunks, embedding_model, index_dir)

    print("Ingestion complete. FAISS index is ready at:", index_dir)