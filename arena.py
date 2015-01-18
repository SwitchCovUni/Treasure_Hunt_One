from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from kivy.config import Config

import main

# Sets the initial window size which will be filled with 20 by 20 blocks
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '780')

# Sets the background tile type
type_list = []

class ArenaMain(Widget):
    layout = FloatLayout(size=(800, 780))
    def update(self):
        pass

    def side_buttons(self):
        rooty = main.Root()

        def open_press(instance):
            rooty.set_sender("arena")
            rooty.show_load()

        # Layout to stack buttons
        side_btn_layout = StackLayout(size_hint_x=None, width=50)

        # Button to open map file
        btn_open = Button(text='Open Map', size_hint=(1, .1))
        btn_open.bind(on_press=open_press)

        side_btn_layout.add_widget(btn_open)

        return side_btn_layout

    def main_arena(self):
        button = Button(
            text='Hello world',
            size_hint=(.5, .25),
            pos=(50, 20))
        self.layout.add_widget(button)
        return self.layout