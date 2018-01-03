import sys
import json
import random
import time

# CLASS TO BE USED IN ANOTHER FILE
# class answer():
#     def __init__(self,mood,mode,rmeter=0):
#         self.mood = mood
#         self.mode = mode
#         self.rmeter = rmeter
#     def annoyance(self):
#         pass 

print("How can I help you?")

go = True

# Reminder to modify things a bit for Android using sys.platform
print "Your os is ",sys.platform

while go == True:
    user = raw_input(">")
    user = user.lower()

    with open("D:/Projects/Ai assistant/answers.json") as cfile:
        command = json.load(cfile)
        for key in command:
            if key in user:
                print (command[key])
                # find a way to use functions inside a json
            # https://stackoverflow.com/questions/2203438/
            # python-how-do-you-call-a-method-when-you-only
            # -have-the-string-name-of-the-metho
    
    # It would be best to add a reference to the ChatterBot library here.