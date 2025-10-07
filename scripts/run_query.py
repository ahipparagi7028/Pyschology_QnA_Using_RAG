from pathlib import Path
from src.rag.pipeline import run_pipeline

if __name__ == "__main__":
    run_pipeline(
        pdf_path=Path("data/book.pdf"),
        queries_path=Path("data/queries.json"),
        output_csv=Path("submission.csv"),
        index_dir=Path("artifacts/index"),
        embedding_model="sentence-transformers/all-MiniLM-L6-v2"
    )