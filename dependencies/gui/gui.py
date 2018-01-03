''' Docstring placeholder. '''

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class MainW(Screen):
    ''' Docstring placeholder. '''
    pass

class Chat(Screen):
    ''' Docstring placeholder.'''
    pass

class Stgs(Screen):
    '''
    Docstring placeholder.
    Make a function to remember on which screen you were before
    you pressed the button to return to it.
    '''
    # def lastscreen(self):
    #     lastscrn = self.root.manager.current
    pass

class Manager(ScreenManager):
    ''' Docstring placeholder. '''
    pass

class KatApp(App):
    ''' Docstring placeholder. '''
    def build(self):
        return Manager()


if __name__ == "__main__":
    KatApp().run()
