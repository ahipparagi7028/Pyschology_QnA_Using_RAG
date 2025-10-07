# My First RAG Project (Psychology Textbook)



This repository contains my very first attempt at building a *Retrieval-Augmented Generation (RAG)* system.  

The goal of this project was not only to implement a working pipeline, but also to help me **learn more about Generative AI and how RAG fits into the broader GenAI ecosystem**.



---



## Motivation



As a Master's student in *Data Analytics and Decision Science* with a growing interest in **Generative AI**, I wanted to build a small project that introduces me to:

\- How to combine external knowledge sources with LLMs,

\- How to store and retrieve context effectively (using FAISS),

\- How to modularize and share a project on GitHub for others to see.



This project is built around a Psychology textbook, which I used as the knowledge base.  

The idea was to ask domain-specific questions and see if the RAG system could return context-aware, grounded answers.



---



## Dataset





The dataset (Psychology textbook) is available as part of the **CASML Generative AI Hackathon** on Kaggle:  

\[CASML Generative AI Hackathon](https://www.kaggle.com/competitions/casml-generative-ai-hackathon)



You will need to download the textbook from Kaggle and place it inside the `data/` folder as `book.pdf`.  

A sample `queries.json` is also expected in the same folder. You can download this from the same website as well.





---



## Usage





1. Clone this repo
   
   ---
2. ### Install Dependencies



pip install -r requirements.txt





### 2\. Ingest textbook into FAISS



python scripts/run\_ingest.py





### 3\. Run queries



python scripts/run\_query.py





*This will produce an output file "submission.csv" with the retrieved context and generated answers.*



---



## Tech Stack



* LangChain — core framework



* SentenceTransformers — embedding model



* FAISS — vector store



* Ollama — local LLM inference



* PyPDF — for document loadign



---



## Notes



* This is my first ever RAG project, built primarily for learning and experimentation. So the code may evolve as I continue learning and improving.



* The project started out as a Jupyter Notebook but is now structured in a modular way to reflect software engineering best practices.



* All vector index and data files are ignored via .gitignore.



* The dataset itself is not included in the repo due to size and licensing. Please obtain it from Kaggle.



* To rebuild the index, simply rerun the ingestion script.



* Use a trusted data source when enabling FAISS deserialization (*allow\_dangerous\_deserialization=True*).



---





## Deprecation Warnings (Langchain v0.2 -> v0.3 Transition)



You may notice warnings like:



*"The class HuggingFaceEmbeddings was deprecated in LangChain 0.2.2"*



This is normal for the current setup.



LangChain recently moved several components into separate packages:



* langchain\_community -> document loaders, vector stores
* langchain\_huggingface -> embeddings
* langchain\_core -> base logic



This project currently uses the **stable 0.2.x line** for simplicity.

Future versions of LangChain will require updating imports (for example):



*"from langchain\_huggingface import HuggingFaceEmbeddings"*



If you see warnings, you can safely ignore them for now - your code will still run correctly.



---



## Future Improvements (Expected mid-November, 2025)



* Migrate to LangChain 0.3+ and langchain-huggingface.
* Add configuration files and logging.
* Introduce unit tests and GitHub Actions for CI/CD.
