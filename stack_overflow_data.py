# load_code_search_net_fixed.py

from datasets import load_dataset
from memory import store_bulk_memories, count_memories

TOTAL_ITEMS = 1500
BATCH_SIZE = 100

MAX_CODE_LEN = 200
MAX_DOC_LEN = 150

print("Loading code_search_net dataset...")

dataset = load_dataset(
    "code_search_net",
    "python",
    split="train[:4000]"
)

batch = []
stored = 0

for i, item in enumerate(dataset):

    if stored >= TOTAL_ITEMS:
        break

    code = item.get("func_code_string", "")
    doc = item.get("func_documentation_string", "")
    name = item.get("func_name", "")

    # Use correct fields
    if isinstance(code, str) and len(code) > 30:

        code = code[:MAX_CODE_LEN]
        doc = doc[:MAX_DOC_LEN]

        memory = f"""
Function Name:
{name}

Documentation:
{doc}

Code:
{code}
"""

        batch.append(memory)

        if len(batch) >= BATCH_SIZE:

            store_bulk_memories(batch)

            stored += len(batch)

            print(f"Stored {stored} memories...")
            print(f"Total memories now: {count_memories()}")

            batch = []

# Store remaining
if batch:

    store_bulk_memories(batch)

    stored += len(batch)

print("✅ Finished storing memories.")
print(f"Final total memories: {count_memories()}")