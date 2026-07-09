print("===== FAQ Chatbot =====")
print("Type 'exit' to stop.")

while True:
    question = input("\nYou: ").lower()

    if question == "hello":
        print("Bot: Hello! How can I help you?")

    elif question == "what is your name":
        print("Bot: I am a FAQ Chatbot.")

    elif question == "how are you":
        print("Bot: I am fine. Thank you!")

    elif question == "what is python":
        print("Bot: Python is a programming language.")

    elif question == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif question == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't know the answer.")