def get_retriever(db, k=5):
    return db.as_retriever(search_type="mmr", search_kwargs={"k": k})