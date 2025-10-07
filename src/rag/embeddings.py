from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_or_load_index(chunks, embedding_model: str, index_dir: Path):
    embedder = HuggingFaceEmbeddings(model_name=embedding_model)
    if index_dir.exists():
        return FAISS.load_local(str(index_dir), embedder, allow_dangerous_deserialization=True)
    db = FAISS.from_documents(chunks, embedder)
    index_dir.mkdir(parents=True, exist_ok=True)
    db.save_local(str(index_dir))
    return db