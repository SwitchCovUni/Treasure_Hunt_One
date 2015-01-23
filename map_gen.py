
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from kivy.config import Config

import main

# Sets the initial window size which will be filled with 20 by 20 blocks
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '780')

# Sets the button type
type_list = []

class MapGenCore(Widget):
    # Initializes the grid layout for the buttons
    layout = GridLayout(cols=40, size_hint_x=None, width=800)

    # List to hold the buttons
    button_list = []

    # Changes the colour of a button according to its assigned type
    def block_colour(self, index):
        if type_list[index] == 1:
            deco = (1.35, 1.93, 1.41, 1)
        elif type_list[index] == 2:
            deco = (0.95, 0.32, 0.32, 1)
        elif type_list[index] == 3:
            deco = (0, 1.02, 1.02, 1)
        elif type_list[index] == 4:
            deco = (2.55, 1.28, 0, 1)
        elif type_list[index] == 5:
            deco = (2.55, 0.28, 0, 1)
        return deco

    def block_refresh(self):
        # Sets all all blocks to their assigned colour
        for n in range(0, 1560):
            self.button_list[n].background_color = self.block_colour(n)

    def block_gen(self):

        # Sets random properties to buttons
        # Later to be replaces with a file
        for n in range(0, 1560):
            type_list.append(1)

        # Button click event function
        def callback(instance):
            # DEBUG DATA PRINT
            print('The button <%s> is being pressed' % instance.text)

            # Stores index from button text
            btn_index = int(instance.text)

            # Adds one or reverts the number to 1 if new num outside of index
            type_list[btn_index] += 1
            if type_list[btn_index] > 5:
                type_list[btn_index] = 1

            # Set colour of clicked button
            instance.background_color = self.block_colour(btn_index)

            # DEBUG DATA PRINT
            print instance.text
            print type_list[btn_index]

        # Adds buttons as widgets to the list
        for n in range(0, 1560):
            self.button_list.append(Button(text=str(n), font_size=14))
            # Button binded to function that allows colour changes
            self.button_list[n].bind(on_press=callback)
            self.button_list[n].background_color = self.block_colour(n)
            self.button_list[n].color = [0, 0, 0, 0]
            self.layout.add_widget(self.button_list[n])

        return self.layout


    def side_buttons(self):
        rooty = main.Root()

        def open_press(instance):
            rooty.set_sender("map")
            rooty.show_load()

        def save_press(instance):
            rooty.show_save()

        # Layout to stack buttons
        side_btn_layout = StackLayout(size_hint_x=None, width=50)

        # Read and write buttons
        btn_open = Button(text='Open', size_hint=(1, .1))
        btn_save = Button(text='Save', size_hint=(1, .1))

        btn_open.bind(on_press=open_press)
        btn_save.bind(on_press=save_press)

        side_btn_layout.add_widget(btn_open)
        side_btn_layout.add_widget(btn_save)

        return side_btn_layout
