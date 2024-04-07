import nltk
from nltk.chat.util import Chat, reflections

# Menggunakan corpus yang telah disediakan oleh NLTK
pairs = [
    ['my name is (.*)', ['Hi %1, how can I help you?']],
    ['(hi|hello|hey|holla)', ['Hello, how can I assist you?']],
    ['(thank you|thanks)', ["You're welcome!", 'No problem.', 'Glad to help!']],
    ['(.*) feel sad', ['Why do you feel sad? Please tell me more.']],
    ['(.*) feel happy', ['I\'m glad to hear that!']],
    ['(.*) your name?', ['I am just a chatbot, you can call me ChatBill.']],
    ['(.*) help (.*)', ['Sure, what can I assist you with?', 'What do you need help with?']],
    ['(.*) your age?', ['I am just a program, so I do not have an age.']],
    ['how are you ?', ['I\'m just a program, but thanks for asking!']],
    ['(.*) (location|city) ?', ['I am an AI and I exist everywhere.']],
    ['(.*) created you?', ['I was created by Bill using Python.']],
    ['(.*)', ['Sorry, I did not understand that.']]
    
]

# Membuat chatbot menggunakan kelas Chat
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm ChatBill. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBill:", response)
        if user_input.lower() == 'exit':
            break

if __name__ == "__main__":
    chat()
