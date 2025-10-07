from pathlib import Path
import json
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path: Path):
    loader = PyPDFLoader(str(pdf_path))
    return loader.load()

def load_queries(queries_path: Path):
    with open(queries_path, "r", encoding="utf-8") as f:
        return json.load(f)
