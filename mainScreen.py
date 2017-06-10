import kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button

#Screen Manager
class SM(ScreenManager):
    def __init__(self, **kwargs):
        super(SM,self).__init__(**kwargs)
        sc = SelectionScreen()
        amScene = AmericanScreen()
        self.add_widget(sc)
        self.add_widget(amScene)

class SelectionScreen(Screen):

    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        layout = FloatL()
        self.add_widget(layout)


class AmericanScreen(Screen):

    def __init__(self, **kwargs):
        super(AmericanScreen, self).__init__(**kwargs)
        

class FloatL(FloatLayout):

    def __init__(self, **kwargs):
        super(FloatL, self).__init__(**kwargs)
        self.cols = 1

        #Page name
        nameLabel = Label(text="Region Selection",
                        color=[1,1,1,1],
                        pos_hint = {'x': 0, 'y':0.4})
        print(nameLabel)
        self.add_widget(nameLabel)

        #Version
        versionLabel = Label(text="Version 1.0.0 Ellard Gerritsen",
                            color=[1,1,1,1],
                            pos_hint={'x': 0, 'y': -0.45})
        self.add_widget(versionLabel)

        #Button configuration
        b1 = Button(text="American Games", 
            pos_hint={'x': 0.40, 'y': 0.5},
            size_hint_x = 0.2,
            size_hint_y = 0.2)
        b1.bind(on_press=self.buttonTest)
        self.add_widget(b1)

        b2 = Button(text="European Games",
             pos_hint={'x': 0.40, 'y': 0.3},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b2.bind(on_press=self.buttonTest)
        self.add_widget(b2)

        b3 = Button(text="Japanese Games",
             pos_hint={'x': 0.40, 'y': 0.1},
             size_hint_x = 0.2,
             size_hint_y = 0.2)
        b3.bind(on_press=self.buttonTest)
        self.add_widget(b3)

    def buttonTest(self,instance):
        print("All good")