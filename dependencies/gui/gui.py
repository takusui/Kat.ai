''' 
This is the GUI for the Android version.
Work in progress.
To do:
- make another .png for the chatbox that scales better
- find a way to add messages
- find a way to keep messages
- find a way to add the transition between chat and microphone (one goes
up and one goes down)

Current problems:
- post button keeps jumping from its original position
- after deleting text from a new line, a space remains that won't allow the 
chat box to go back to its original size

'''
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

lastscreen = 'main'

class MainW(Screen):
    pass

class Chat(Screen):
    pass

class Stgs(Screen):
    pass

class Manager(ScreenManager):
    pass

class KatApp(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    KatApp().run()