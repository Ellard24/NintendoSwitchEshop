

#Python Kivy Project

import kivy
from kivy.app import App
import mainScreen


#Main loop of Application
class MyApp(App):

    def build(self):
        self.title = "Nintendo Switch App"
        home = mainScreen.SM()
        return home

    def on_stop(self):
        pass

if __name__ == '__main__':
    MyApp().run()