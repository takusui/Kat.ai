''' 
Kat's GUI uses kivy 1.10.0.
The apparel code is in the kat.kv file.
Find a way to swap between microphone and chat.
Maybe add an animation that will bring the microphone
down in the bar and move the chat up, occupying half
of the page.
'''

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainW(Screen):
    pass

class Chat(Screen):
    pass

class Stgs(Screen):
    '''
    Make a function to remember on which screen you were before
    you pressed the button to return to it.
    '''
    pass

class Manager(ScreenManager):
    pass

class KatApp(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    KatApp().run()
