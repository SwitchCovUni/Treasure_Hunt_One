from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.config import Config


# Sets the initial window size which will be filled with 20 by 20 blocks
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '780')

layout = GridLayout(cols=40, size_hint_x=None, width=850)
class Arena_Main(Widget):


    # Loop for robot movement and interactions etc
    # Clock.schedule_interval(self.update, 1.0 / 60.0)
    def update(self):
        pass


    def start_arena(self):
        button = Button(text='This is a', font_size=14)

        button2 = Button(text='test page', font_size=14)
        layout.add_widget(button)
        layout.add_widget(button2)

        return layout