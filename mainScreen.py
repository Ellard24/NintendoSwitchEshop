import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

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
            pos_hint={'x': 0.1, 'y': 0.45},
            size_hint_x = 0.2,
            size_hint_y = 0.2)
        b1.bind(on_press=lambda *args: self.changePage('second'))
        layout.add_widget(b1)

        b2 = Button(text="European Games",
             pos_hint={'x': 0.40, 'y': 0.45},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b2.bind(on_press=lambda *args: self.changePage('third'))
        layout.add_widget(b2)

        b3 = Button(text="Japanese Games",
             pos_hint={'x': 0.70, 'y': 0.45},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b3.bind(on_press=lambda *args: self.changePage('fourth'))
        layout.add_widget(b3)

        self.add_widget(layout)
    
    def buttonTest(self, screenName):
        print(screenName)
        requester = pyRequests.webRequest()
        print(requester.makeRequest('https://secret-depths-21261.herokuapp.com/'))

    def changePage(self,screenName):
        print(screenName)
        self.manager.current = screenName


class AmericanScreen(Screen):

    def __init__(self, **kwargs):
        super(AmericanScreen, self).__init__(**kwargs)

        requester = pyRequests.webRequest()
        newData = requester.makeRequest('https://secret-depths-21261.herokuapp.com/')
        
        #print(len(newData['results']))
        #print(newData['results'][0]['game']['title'])

        floater = FloatLayout(size_hint=(1, 1))

        #Create the scrollview
        scroller = ScrollView(size_hint=(.7, .7) ,
                pos_hint={'center_x': .55, 'center_y': .5}, do_scroll_x=False)
        
        layout = GridLayout(cols=1, padding=10, spacing=10,
                size_hint=(None, None), width=500)
        layout.bind(minimum_height=layout.setter('height'))
        
        #image
        backImage = Image(source='background2.png', allow_stretch = True, keep_ratio = False)
        floater.add_widget(backImage)

        

        #Create a back button
        b1 = Button(text="Back",
                    pos_hint={'x': 0, 'y': 0},
                    size_hint_x = 0.1,
                    size_hint_y = 0.1)
        b1.bind(on_press = lambda *args: self.goBack('first'))
        floater.add_widget(b1)

        for i in range(len(newData['results'])):
            btn = Button(text=str(newData['results'][i]['game']['title']), size_hint_y=None, height=40)
            layout.add_widget(btn)

        scroller.add_widget(layout)
        floater.add_widget(scroller)
        self.add_widget(floater)
        


    def goBack(self, screenName):
        self.manager.current = screenName

    def buttonTest(self, screenName):
        print(screenName)
        requester = pyRequests.webRequest()
        print(requester.makeRequest('https://secret-depths-21261.herokuapp.com/'))

class EuropeanScreen(Screen):

    def __init__(self, **kwargs):
        super(EuropeanScreen, self).__init__(**kwargs)

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