import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

#temporary test
import pyRequests

#Screen Manager
class SM(ScreenManager):
    def __init__(self, **kwargs):
        super(SM,self).__init__(**kwargs)
        sc = SelectionScreen(name="first")
        amScreen = AmericanScreen(name='second')
        eurScreen = EuropeanScreen(name='third')
        japScreen = JapaneseScreen(name='fourth')

        self.add_widget(sc)

        #adding widget screens
        self.add_widget(amScreen)
        self.add_widget(eurScreen)
        self.add_widget(japScreen)

    def screenChanger():
        print("Function was called")

'''
Main Selection Screen for picking the region
'''
class SelectionScreen(Screen):

    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        #button and label placement
        #Page name
        nameLabel = Label(text="Region Selection",
                        color=[1,1,1,1],
                        pos_hint = {'x': 0, 'y':0.4})
        print(nameLabel)
        layout.add_widget(nameLabel)

        #Version
        versionLabel = Label(text="Version 1.0.0 Ellard Gerritsen",
                            color=[1,1,1,1],
                            pos_hint={'x': 0, 'y': -0.45})
        layout.add_widget(versionLabel)

        #Button configuration
        b1 = Button(text="American Games", 
            pos_hint={'x': 0.40, 'y': 0.5},
            size_hint_x = 0.2,
            size_hint_y = 0.2)
        b1.bind(on_press=lambda *args: self.buttonTest('first'))
        layout.add_widget(b1)

        b2 = Button(text="European Games",
             pos_hint={'x': 0.40, 'y': 0.3},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b2.bind(on_press=lambda *args: self.buttonTest('second'))
        layout.add_widget(b2)

        b3 = Button(text="Japanese Games",
             pos_hint={'x': 0.40, 'y': 0.1},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b3.bind(on_press=lambda *args: self.buttonTest('third'))
        layout.add_widget(b3)

        self.add_widget(layout)
    
    def buttonTest(self, screenName):
        print(screenName)
        requester = pyRequests.webRequest()
        print(requester.makeRequest('https://secret-depths-21261.herokuapp.com/'))


class AmericanScreen(Screen):

    def __init__(self, **kwargs):
        super(AmericanScreen, self).__init__(**kwargs)
    

class EuropeanScreen(Screen):

    def __init__(self, **kwargs):
        super(EuropeanScreen, self).__init__(**kwargs)

class JapaneseScreen(Screen):

    def __init__(self, **kwargs):
        super(JapaneseScreen, self).__init__(**kwargs)