import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image, AsyncImage
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

#clock
from kivy.clock import Clock
from functools import partial

#webbrowser
import webbrowser

#temporary test
import pyRequests

#individual screen widgets
import amerScreen
import euroScreen
import japanScreen
import gameScreen

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

        gamScreen = gameScreen.GameScreen(name='fifth')

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
        layout.add_widget(nameLabel)

        #RSS Feed Laebl

        rssLabel = Label(text="Newest Switch News", 
                        color=[1,1,1,1],
                        pos_hint={'x': 0, 'y': -.12})
        layout.add_widget(rssLabel)

        #Version label
        versionLabel = Label(text="Version 1.0.0 Ellard Gerritsen",
                            color=[1,1,1,1],
                            pos_hint={'x': .35, 'y': -0.45})
        layout.add_widget(versionLabel)

        #Button configuration for Region Selection
        b1 = Button(text="Game List", 
            pos_hint={'center_x': 0.5, 'center_y': 0.50},
            size_hint_x = 0.3,
            size_hint_y = 0.1)
        b1.bind(on_press=lambda *args: self.changePage('second'))
        layout.add_widget(b1)

        '''
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
        '''

        #Add the Scrollview which contains the RSS Feed Information
        RSS = RSSFeedView(size_hint=(1, .2) ,
                pos_hint={'center_x': .55, 'center_y': .25}, do_scroll_x=False)
        rssList = RSS.parseFeed("http://www.nintendolife.com/feeds/latest")
        
        grid = GridLayout(cols=1, padding=0, spacing=0,
                size_hint=(None, None), width=700)
        grid.bind(minimum_height=grid.setter('height'))

        #Add a button for each item in the RSS list and bind the appropriate function
        for i in range(len(rssList)):
            btn = Button(text=str(rssList[i][0]),size_hint_x = 1,size_hint_y=None, height=30,
                        background_color=[.5,.5,.5,1])
            btn.bind(on_press=partial(self.setHyperLink, rssList[i][1]))
            grid.add_widget(btn)

        #Add widgets to their parents
        RSS.add_widget(grid)
        layout.add_widget(RSS)

        self.add_widget(layout)
    
    #This function allows user to press on each button to open the corresponding hyperlink
    def setHyperLink(self, url, *args):
        webbrowser.open(url)

    #Changes page based on Region button pressed
    def changePage(self,screenName):
        print(screenName)
        self.manager.current = screenName





#This probably doesnt need its own class
class RSSFeedView(ScrollView):

    def __init__(self, **kwargs):
        super(RSSFeedView, self).__init__(**kwargs)
        self.info = []

    #This is probably overkill and can later be removed
    def parseFeed(self,url):
        
        feeder = pyRequests.webRequest()
        self.info = feeder.getFeed(url)
        return self.info





