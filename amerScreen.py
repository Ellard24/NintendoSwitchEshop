#American Screen
import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

import pyRequests

class AmericanScreen(Screen):

    def __init__(self, **kwargs):
        super(AmericanScreen, self).__init__(**kwargs)

        #Sends a request to my API hosted on heroku which has all the details that we need
        requester = pyRequests.webRequest()
        newData = requester.makeRequest('https://secret-depths-21261.herokuapp.com/')
        
        #print(len(newData['results']))
        #print(newData['results'][0]['game']['title'])

        floater = FloatLayout(size_hint=(1, 1))

        #Create the scrollview to be only a certain portion of the Application window
        scroller = ScrollView(size_hint=(.7, .7) ,
                pos_hint={'center_x': .55, 'center_y': .5}, do_scroll_x=False)
        
        layout = GridLayout(cols=1, padding=10, spacing=10,
                size_hint=(None, None), width=500)
        layout.bind(minimum_height=layout.setter('height'))
        
        #Sets up background image and stretches image to fit screen
        backImage = Image(source='background2.png', allow_stretch = True, keep_ratio = False)
        floater.add_widget(backImage)

        

        #Create a back button and append it to background layout
        b1 = Button(text="Back",
                    pos_hint={'x': 0, 'y': 0},
                    size_hint_x = 0.1,
                    size_hint_y = 0.1)
        b1.bind(on_press = lambda *args: self.goBack('first'))
        floater.add_widget(b1)

        #Create a button for each game in the list and append to scrollview layout
        for i in range(len(newData['results'])):
            btn = Button(text=str(newData['results'][i]['game']['title']), size_hint_y=None, height=40)
            layout.add_widget(btn)

        #Append all widgets to their appropriate parent
        scroller.add_widget(layout)
        floater.add_widget(scroller)
        self.add_widget(floater)
        

    #We want to expand a box below the button pressed which will contain all the info about a certain game
    def expandInfo(self, game):
        pass

    #Returns to selection screen using screen manager 
    def goBack(self, screenName):
        self.manager.current = screenName