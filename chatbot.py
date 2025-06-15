import random
import re
"""
Triggers

hello
What is hangman
what is your portfolio?
Hero prabhas 
thanks

"""

responses = {
    r"\bhello\b|\bhi\b|\bhey\b": [
        "Hello there! How can I help you today?",
        "Hi! What would you like to know?"
    ],
    r"\bhow are you\b|\bhru\b": [
        "I’m just a bunch of code, but I’m running smoothly!",
        "Doing great—thanks for asking!"
    ],
    r"\bhangman\b": [
        "Hangman is a console‑based Python game where you guess letters to reveal a hidden word.",
        "My Hangman game picks a random word and gives you 6 lives to guess it one letter at a time."
    ],
    r"\bportfolio\b": [
        "My portfolio site showcases my projects in Python and Java, plus my startup details.",
        "You can view my work here : github.com/rakesh-donga"
    ],
    r"\bchatbot\b": [
        "This chatbot is a simple Q&A bot using keyword matching in Python.",
        "I built this basic chatbot to demonstrate input parsing and response selection."
    ],
    r"\bprabhas\b|\bhero\b": [
        "A dinosour in telugu film industry",
        "An tollywood actor with a lot fan following"
    ],
    r"\bthank you\b|\bthanks\b": [
        "You’re welcome!",
        "Glad I could help!"
    ],
}

default_replies = [
    "Sorry, I didn’t understand that. Could you rephrase?",
    "I’m not sure I follow—ask me about Hangman, or Prabhas!"
]

def get_response(message: str) -> str:
    msg = message.lower()
    for pattern, replies in responses.items():
        if re.search(pattern, msg):
            return random.choice(replies)
    return random.choice(default_replies)

def chat():
    print("Chatbot: 👋 Hello! I am chatbot ask me something. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Chatbot: Goodbye! 👋")
            break
        reply = get_response(user_input)
        print("Chatbot:", reply)

if __name__ == "__main__":
    chat()
