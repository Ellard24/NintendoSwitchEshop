#Game Screen
import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout

#clock
from kivy.clock import Clock
from functools import partial

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
        #floater.add_widget(b1)
        self.add_widget(b1)

        self.add_widget(floater)

        #Display all the relavent info
    def goBack(self, screenName):
        self.manager.current = screenName

    def on_enter(self, *args):
        print("entered gameScreen")
        #print(self.parent.gameName)

        #Add labels for all the data
        try:
            gName = Label(text=str(self.parent.gameName['title']), pos_hint={'x': 0, 'center_y': .4})
        except:
            gName = Label(text="Undefined", pos_hint={'x': 0, 'center_y': .4})
        try:
            gPrice = Label(text= "$" + str(self.parent.gameName['price']), pos_hint={'x': 0, 'center_y': .3})
        except:
            gPrice = Label(text="Undefined", pos_hint={'x': 0, 'center_y': .3})
        try:
            gDate = Label(text=str(self.parent.gameName['releaseDate']), pos_hint={'x': 0, 'center_y': .2})
        except:
            gDate = Label(text="Undefined", pos_hint={'x': 0, 'center_y': .2})
        try:
            gURL = self.parent.gameName['art']
            gImage = AsyncImage(source= gURL, pos_hint={'x': 0, 'center_y': .7})
        except:
            gImage = Image(source="imageError.png",pos_hint={'x': 0, 'center_y': .7})

        self.children[0].add_widget(gName)
        self.children[0].add_widget(gPrice)
        self.children[0].add_widget(gDate)
        self.children[0].add_widget(gImage)
        
    def on_pre_leave(self):
        self.children[0].clear_widgets()