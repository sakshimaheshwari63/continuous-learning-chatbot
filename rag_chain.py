import google.generativeai as genai
from memory import store_memory, retrieve_memories

# Configure API
genai.configure(api_key="AIzaSyD1rrGToqOF4BJHz7NVBPNFvCGCrnRjFqY")

# ✅ Use valid model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_response(user_input):

    # Retrieve context
    memories = retrieve_memories(user_input, k=5)

    context = "\n".join(memories)

    prompt = f"""
You are an AI assistant with memory.

Context:
{context}

User Question:
{user_input}

Answer clearly:
"""

    response = model.generate_content(prompt)

    answer = response.text

    # Store memory
    store_memory(f"User: {user_input}\nAssistant: {answer}")

    return answer