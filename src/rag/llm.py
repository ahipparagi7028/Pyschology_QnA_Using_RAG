import ollama

def run_llm(prompt: str, model: str = "tinyllama") -> str:
    resp = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return resp.get("message", {}).get("content", "")