import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

print("🤖 AI Chatbot with Memory (type 'exit' to quit)\n")

# 🧠 Chat history
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye 👋")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.7
    )

    answer = response.choices[0].message.content

    # Add bot response to history
    messages.append({"role": "assistant", "content": answer})

    print(f"Bot: {answer}\n")
