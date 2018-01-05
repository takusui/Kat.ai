'''
The brain of Kat.
To be added:
- tell the time in another country
- tell the weather in another city (https://dialogflow.com/docs/getting-started/basics)
- find a way to use her without having to train everytime on startup
'''

# import json
from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer


# CLASS TO BE USED IN ANOTHER FILE
# class answer():
#     def __init__(self,mood,mode,rmeter=0):
#         self.mood = mood
#         self.mode = mode
#         self.rmeter = rmeter
#     def annoyance(self):
#         pass

kat = ChatBot(
    'Kat',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
    )

# Reminder to modify things a bit for Android using sys.platform

def answer(user):
    try:
        iscomm = False

        # with open("D:/Projects/Ai assistant/answers.json") as cfile:
        #     command = json.load(cfile)
        #     for key in command:
        #         if key in user:
        #             print command[key]
        #             iscomm = True

        #         # find a way to use functions inside a json
        #         # https://stackoverflow.com/questions/2203438/
        #         # python-how-do-you-call-a-method-when-you-only
        #         # -have-the-string-name-of-the-metho

        if not iscomm:
            response = kat.get_response(user)
            return response

    except (KeyboardInterrupt, EOFError, SystemExit):
        return 'Error while processing answer.'

# Debugging starts here.
while True:
    user_inp = raw_input('> ')
    if user_inp == 'exit':
        exit()
    else:
        print answer(user_inp)
