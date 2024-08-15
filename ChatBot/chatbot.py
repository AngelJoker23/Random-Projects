# Importing libraries
from nltk.chat.util import Chat, reflections

responses = [
    [
        r"(hi|hey|hello|hola|holla).(.*)",
        ["Hello", "Hey there", "Hello user", "Hello Friend"]
    ],

    [
        r"(.*) your name?",
        ["My name is Ninja and I'm a chatbot.",]
    ],

    [
        r"how are you (.*)?",
        ["I am great!, I am fine., I am good."]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that",]
    ],

    [
        r"quit",
        ["Bye. See you soon :)", "Have a great day. See you soon :)",
            "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That was nice to hear']
    ],
]

# Generating reflections
print(reflections)

# Output
{
    'i': 'you',
    'your': 'my',
    'yours': 'mine',
    'i was': 'you were',
    'you were': 'i was',
    "i'll": 'you will',
    "you'll": 'i will',
    'you are': 'I am',
    "you've": 'I have',
    "I'd": 'you would'
}

# Default message
print("Hi, I'm a bot, and my name is Ninja. \nPlease type your query. Type quit to leave.")
# Creating Chat Bot
chat = Chat(responses, reflections)

# To start a conversation with the chatbot
chat.converse()
