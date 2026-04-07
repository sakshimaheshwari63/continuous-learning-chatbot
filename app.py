# app.py

from rag_chain import generate_response

print("\n🧠 Continuous Learning Gemini Chatbot Started")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    reply = generate_response(user_input)
    print("\nBot:", reply, "\n")