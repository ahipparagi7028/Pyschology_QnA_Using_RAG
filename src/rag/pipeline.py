from pathlib import Path
import csv, json
from .data_loader import load_pdf, load_queries
from .chunking import chunk_documents
from .embeddings import build_or_load_index
from .retriever import get_retriever
from .llm import run_llm

def run_pipeline(pdf_path: Path, queries_path: Path, output_csv: Path,
                 index_dir: Path, embedding_model: str, chunk_size=1000,
                 chunk_overlap=200, retriever_k=5, llm_model="tinyllama"):
    
    docs = load_pdf(pdf_path)
    chunks = chunk_documents(docs, chunk_size, chunk_overlap)
    db = build_or_load_index(chunks, embedding_model, index_dir)
    retriever = get_retriever(db, retriever_k)
    queries = load_queries(queries_path)

    with open(output_csv, "w", newline="", encoding="utf-8") as out_f:
        writer = csv.DictWriter(out_f, fieldnames=["ID", "answer", "references"])
        writer.writeheader()
        for q in queries:
            qid = q["query_id"]
            question = q["question"]
            docs = retriever.get_relevant_documents(question)
            context = "\n\n".join([d.page_content for d in docs])
            refs = [d.metadata for d in docs]

            prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
            answer = run_llm(prompt, model=llm_model)

            writer.writerow({"ID": qid, "answer": answer, "references": json.dumps(refs)})