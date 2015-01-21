from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from kivy.config import Config
from kivy.graphics import Color, Rectangle
import main

# Sets the initial window size which will be filled with 20 by 20 blocks
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '780')

# Sets the background tile type
type_list = []

class Tiles(FloatLayout):
    def __init__(self, **kwargs):
        super(Tiles, self).__init__(**kwargs)

        # Creates a blank canvas ready for loading
        for n in range(0, 1560):
            type_list.append(0)

        # Variables used for creating the blocks
        xpos = 50
        ypos = 760
        place_in_row = 1

        for n in type_list:

            with self.canvas:
                # Add a red color
                # TODO add sprites
                Color(1., 0, 0)

                # Add a rectangle
                Rectangle(pos=(xpos, ypos), size=(20, 20))

            # Once the blocks get to row 40 start a new line
            if place_in_row == 40:
                print "test"
                place_in_row = 1
                ypos -= 20
                xpos = 50
                print ypos
            else:
                place_in_row += 1
                xpos += 20


class ArenaMain(Widget):

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

    def main_arena(self):
        return Tiles()
