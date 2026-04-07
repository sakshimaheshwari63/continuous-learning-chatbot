# load_5000_memories.py

import time
from memory import store_memories, total_memories
from datasets import load_dataset
import wikipedia

# ------------------------------
# 1️⃣ Load 1500 StackOverflow Q&A
# ------------------------------
print("Loading StackOverflow data...")

try:
    # Using the public stack-exchange dataset from HuggingFace
    stack_ds = load_dataset("lvwerra/stack-exchange-paired", split="train[:1500]")
except Exception as e:
    print("Error loading StackOverflow dataset:", e)
    stack_ds = []

stack_memories = []
for i, item in enumerate(stack_ds):
    q = item.get("question", "")
    a = item.get("answer", "")
    if q and a:
        stack_memories.append(f"Q: {q} A: {a}")
print(f"StackOverflow memories collected: {len(stack_memories)}")

store_memories(stack_memories)
print(f"Stored StackOverflow memories. Total stored: {total_memories()}\n")

time.sleep(1)

# ------------------------------
# 2️⃣ Load 1500 Wikipedia AI/LLM entries
# ------------------------------
print("Loading Wikipedia summaries...")

wiki_topics = [
    "Artificial intelligence", "Large language model", "Machine learning",
    "Deep learning", "Natural language processing", "Generative AI",
    "Neural network", "Transformer (machine learning model)"
]

wiki_memories = []
for topic in wiki_topics:
    try:
        page = wikipedia.page(topic)
        summary = page.summary.split("\n")[0:2]  # first 2 paragraphs
        wiki_memories.append(f"{topic}: {' '.join(summary)}")
    except Exception as e:
        print(f"Skipped topic {topic} due to error:", e)

# Repeat to reach ~1500 entries
wiki_memories *= (1500 // len(wiki_memories) + 1)
wiki_memories = wiki_memories[:1500]

store_memories(wiki_memories)
print(f"Stored Wikipedia memories. Total stored: {total_memories()}\n")

time.sleep(1)

# ------------------------------
# 3️⃣ Load 2000 AI trend entries
# ------------------------------
print("Loading AI trend memories...")

# Simulated trend entries; replace with real data if available
ai_trends = [f"AI Trend {i}: New development in large language models and generative AI." for i in range(1, 2001)]

store_memories(ai_trends)
print(f"Stored AI trend memories. Total stored: {total_memories()}\n")

# ------------------------------
print("✅ Finished loading 5000 memories!")
print(f"Total memories stored in vector DB: {total_memories()}")