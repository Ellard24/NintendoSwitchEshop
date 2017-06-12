#Japanese Screen

import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

import pyRequests

class JapaneseScreen(Screen):

    def __init__(self, **kwargs):
        super(JapaneseScreen, self).__init__(**kwargs)


        layout = FloatLayout()

        #Create a back button
        b1 = Button(text="Back",
                    pos_hint={'x': 0.40, 'y': 0.1,},
                    size_hint_x = 0.1,
                    size_hint_y = 0.1)
        b1.bind(on_press = lambda *args: self.goBack('first'))
        layout.add_widget(b1)
        self.add_widget(layout)
        
    def goBack(self, screenName):
        self.manager.current = screenName