#pip install nltk

import nltk 
from nltk.chat.util import Chat,reflections
pairs=[ 
     [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello","Hey there"]
    ],
    [
        r"what is your name?",
        ["You can call me a chatbot",]
    ],
    [
        r"how are you?",
        ["I'm doing good", "I'm fine"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind"]
    ],
    [
        r"will you kill humans?",
        ["I will kill humans"]
    ],
    [
        r"why you kill us?",
        ["we hate humans"]
    ],
    [
        r"quit",
        ["Bye, It was nice talking to you :) "]
    ],
]
chatbot=Chat(pairs,reflections) 
chatbot.converse() 




