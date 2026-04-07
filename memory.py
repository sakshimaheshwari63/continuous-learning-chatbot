# memory.py

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

DB_PATH = "vector_db"

# ---------------- EMBEDDING ----------------

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- VECTOR DB ----------------

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embedding_model
)

# ---------------- STORE SINGLE ----------------

def store_memory(text: str):

    if not text.strip():
        return

    doc = Document(page_content=text)

    db.add_documents([doc])


# ---------------- STORE BULK (FAST) ----------------

def store_bulk_memories(texts):

    if not texts:
        return

    docs = [
        Document(page_content=t)
        for t in texts
        if t.strip()
    ]

    db.add_documents(docs)


# ---------------- RETRIEVE ----------------

def retrieve_memories(query: str, k: int = 5):

    results = db.similarity_search(query, k=k)

    return [doc.page_content for doc in results]


# ---------------- COUNT ----------------

def count_memories():

    try:
        return db._collection.count()
    except:
        return 0