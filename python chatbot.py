
import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define pairs of patterns and corresponding responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by John Doe. You can call me ChatBot."]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you! How are you?", "Doing great! What about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No worries at all."]
    ],
    [
        r"i'm (.*) doing good",
        ["I'm glad to hear that!", "That's great to hear!"]
    ],
    [
        r"what do you do ?",
        ["I chat with people and assist them!", "I'm here to talk with you."]
    ],
    [
        r"who created you ?",
        ["I was created by John Doe using Python and NLTK.", "I am a project of John Doe."]
    ],
    [
        r"(.*) your favorite color ?",
        ["I don't have preferences, but I like blue!", "I think all colors are beautiful."]
    ],
    [
        r"(.*) weather in (.*)",
        ["I don't know the weather in %2, but you can check it online!", "You should check the weather in %2 on a weather app."]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day.", "Take care! Goodbye!"]
    ]
]

# Create a chatbot object with pattern-response pairs
def chatbot():
    print("ChatBot: Hello! Type 'quit' to exit the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Main program to run the chatbot
if __name__ == "__main__":
    chatbot()
