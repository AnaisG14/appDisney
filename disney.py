import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui.page1 import Page1
from ui.page2 import Page2
import ui.widgets as _  # noqa


kivy.require('2.3.1')   # replace with your current kivy version !
Window.size = (360, 640)


class DisneyApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Page1(name='page1'))
        sm.add_widget(Page2(name='page2'))
        return sm


if __name__ == '__main__':
    DisneyApp().run()
