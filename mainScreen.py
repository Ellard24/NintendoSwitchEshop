import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button


class SelectionScreen(Screen):

    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        layout = Grid()
        self.add_widget(layout)

class Grid(GridLayout):

    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        #Button configuration
        b1 = Button(text="American Games", pos=(self.x, self.height / 2))
        b1.bind(on_press=self.buttonTest)
        self.add_widget(b1)

        b2 = Button(text="European Games", pos=(self.x, self.height / 2))
        b2.bind(on_press=self.buttonTest)
        self.add_widget(b2)

        b3 = Button(text="Japanese Games", pos=(self.x, self.height / 2))
        b3.bind(on_press=self.buttonTest)
        self.add_widget(b3)

    def buttonTest(self,instance):
        print("All good")