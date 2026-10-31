
# DecodeLabs - Project 1
# Rule-Based AI Chatbot

def start_chatbot():

    responses = {
        # Greetings
        "hello": "Hello! Welcome to DecodeLabs AI.",
        "hi": "Hi! How can I help you?",
        "hey": "Hey! Nice to meet you.",
        "good morning": "Good morning! Have a productive day!",
        "good night": "Good night! See you soon!",

        # General conversation
        "how are you": "I'm functioning perfectly!",
        "what is your name": "I am the DecodeLabs AI Chatbot.",
        "what is your purpose": "My purpose is to demonstrate rule-based conversations using Python.",
        "who developed you": "I was developed as a project for the DecodeLabs AI internship.",
        "what can you do": "I can answer predefined questions and respond to greetings.",

        # AI and programming
        "what is ai": "AI stands for Artificial Intelligence.",
        "what is python": "Python is a high-level programming language.",
        "how python works": "Python executes code through its interpreter, which processes your instructions and runs the program.",
        "how does python work": "Python executes code through its interpreter, which processes your instructions and runs the program.",
        "what is machine learning": "Machine learning enables computers to learn patterns from data.",
        "what is a chatbot": "A chatbot is a program that communicates with users through predefined rules or AI models.",

        # Help and thanks
        "help": "Try asking: hello, what is AI, what is Python, how Python works, or what is a chatbot.",
        "thank you": "You're welcome!",
        "thanks": "Happy to help!"
    }

    exit_commands = ["exit", "bye", "quit"]

    print("\n" + "=" * 45)
    print("       DECODELABS AI CHATBOT")
    print("=" * 45)
    print("Type 'help' for assistance.")
    print("Type 'exit', 'bye', or 'quit' to stop.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if not user_input:
            print("Bot: Please enter a message.")
            continue

        if user_input in exit_commands:
            print("Bot: Goodbye! Have a great day!")
            break

        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: I don't understand that yet. Type 'help'.")

if __name__ == "__main__":
    start_chatbot()