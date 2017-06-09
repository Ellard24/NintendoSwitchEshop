

#Python Kivy Project

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import mainScreen
import american



#Screen Manager
class SM(ScreenManager):
    def __init__(self, **kwargs):
        super(SM,self).__init__(**kwargs)
        sc = mainScreen.SelectionScreen()
        amScene = american.AmericanScene()
        self.add_widget(sc)


#Main loop of Application
class MyApp(App):

    def build(self):
        self.title = "Nintendo Switch App"
        home = SM()
        return home

    def on_stop(self):
        print("Bye")

if __name__ == '__main__':
    MyApp().run()