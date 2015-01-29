from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

import main

# Sets the initial window size which will be filled with 20 by 20 blocks
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '780')

# Sets the background tile type
type_list = []


class ArenaMain(Widget):
    arena_layout = GridLayout(cols=40, size_hint_x=None, width=800, size_hint_y=None, height= 780)

    # List to hold the buttons
    block_list = []

    def load_blocks(self):
        self.arena_layout.clear_widgets()
        self.block_list[:] = []
        for n in range(0, 1560):

            if type_list[n] == 1:
                self.block_list.append(Image(source='Resources/floorSprite.png'))
            elif type_list[n] == 2:
                self.block_list.append(Image(source='Resources/wallSprite.png'))
            elif type_list[n] == 3:
                self.block_list.append(Image(source='Resources/smallTreasure1.png'))

            self.arena_layout.add_widget(self.block_list[n])



    def start(self):

        # Creates a blank canvas ready for loading
        for n in range(0, 1560):
            type_list.append(0)

        # Adds buttons as widgets to the list
        for n in range(0, 1560):
            self.block_list.append(Image(source='Resources/smallTreasure1.png'))
            self.arena_layout.add_widget(self.block_list[n])

        return self.arena_layout

    def side_buttons(self):
        rooty = main.Root()

        def open_press(instance):
            rooty.set_sender("arena")
            rooty.show_load()

        # Layout to stack buttons
        side_btn_layout = StackLayout(size_hint_x=None, width=50)

        # Button to open map file
        btn_open = Button(text='Open', size_hint=(1, .1))
        btn_open.bind(on_press=open_press)

        side_btn_layout.add_widget(btn_open)

        return side_btn_layout

