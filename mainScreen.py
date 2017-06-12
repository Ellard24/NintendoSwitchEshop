import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

#clock
from kivy.clock import Clock
from functools import partial


#temporary test
import pyRequests

#individual screen widgets
import amerScreen
import euroScreen
import japanScreen

#Screen Manager
class SM(ScreenManager):

    gameName = "Not set"

    def __init__(self, **kwargs):
        super(SM,self).__init__(**kwargs)
        #self.gameName = "Empty for now"
        sc = SelectionScreen(name="first")
        amScreen = amerScreen.AmericanScreen(name='second')
        eurScreen = euroScreen.EuropeanScreen(name='third')
        japScreen = japanScreen.JapaneseScreen(name='fourth')

        gamScreen = GameScreen(name='fifth')

        self.add_widget(sc)

        #adding widget screens
        self.add_widget(amScreen)
        self.add_widget(eurScreen)
        self.add_widget(japScreen)
        self.add_widget(gamScreen)
    
    def testFunction(self):
        print("Test called")

'''
Main Selection Screen for picking the region
'''
class SelectionScreen(Screen):

    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        #Background image
        backImage = Image(source='background.png', allow_stretch = True, keep_ratio = False)
        layout.add_widget(backImage)


        #button and label placement
        #Page name
        nameLabel = Label(text="Region Selection",
                        color=[1,1,1,1],
                        pos_hint = {'x': 0, 'y':0.4},
                        font_size = 30)
        print(nameLabel)
        layout.add_widget(nameLabel)

        #Version
        versionLabel = Label(text="Version 1.0.0 Ellard Gerritsen",
                            color=[1,1,1,1],
                            pos_hint={'x': .35, 'y': -0.45})
        layout.add_widget(versionLabel)

        #Button configuration
        b1 = Button(text="American Games", 
            pos_hint={'x': 0.1, 'y': 0.40},
            size_hint_x = 0.2,
            size_hint_y = 0.2)
        b1.bind(on_press=lambda *args: self.changePage('second'))
        layout.add_widget(b1)

        b2 = Button(text="European Games",
             pos_hint={'x': 0.40, 'y': 0.40},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b2.bind(on_press=lambda *args: self.changePage('third'))
        layout.add_widget(b2)

        b3 = Button(text="Japanese Games",
             pos_hint={'x': 0.70, 'y': 0.40},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b3.bind(on_press=lambda *args: self.changePage('fourth'))
        layout.add_widget(b3)

        self.add_widget(layout)

    def changePage(self,screenName):
        print(screenName)
        self.manager.current = screenName

class GameScreen(Screen):
    
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

        #Create a layout for the page
        floater = FloatLayout(size_hint=(1, 1))
        #Back button
        b1 = Button(text="Back",
                    pos_hint={'x': 0, 'y': 0},
                    size_hint_x = 0.1,
                    size_hint_y = 0.1)
        b1.bind(on_press = lambda *args: self.goBack('second'))
        floater.add_widget(b1)
        self.add_widget(floater)

        #Display all the relavent info
    def goBack(self, screenName):
        self.manager.current = screenName

    def on_enter(self, *args):
        print("entered gameScreen")
        print(self.parent.gameName)

    def printInfo(self):
        pass