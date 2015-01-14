from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from kivy.uix.screenmanager import ScreenManager, Screen

import os

# Import modules
import map_gen
import arena

# Sets the initial window size which will be filled with 20 by 20 blocks
Config.set('graphics', 'width', '850')
Config.set('graphics', 'height', '780')

# Store the different screens
sm = ScreenManager()

# Loads widgets child widgets of LoadDialog from Treasure_Hunt.kv
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


# Loads widgets child widgets of SaveDialog from Treasure_Hunt.kv
class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    # Generic library code to close the current dialogue
    def dismiss_popup(self):
        self._popup.dismiss()

    # Generic library code for the load dialogue
    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    # Generic library code for the save dialogue
    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        # Loads file into a stream ready for reading
        with open(os.path.join(path, filename[0])) as stream:
            core = map_gen.MapGenCore()

            # Unpacks stream to a stream
            loadable = stream.read()

            # Loop splits file characters into the list
            count = 0
            for n in loadable:
                map_gen.type_list[count] = int(loadable[count])
                count += 1

            # Refresh the button matrix
            core.block_refresh()

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:

            printable = ""

            # Converts the array of chars to a string
            for n in range(0, 1560):
                printable += str(map_gen.type_list[n])

            # Uses string to write the file
            stream.write(printable)

        self.dismiss_popup()

class MenuCore(Widget):
    def menu_screen_layout(self):
        def map_screen(self):
            sm.current = 'mapgen'
        def arena_screen(self):
            sm.current = 'arenascreen'

        layout = GridLayout(cols=2)
        button = Button(text='MapGen', font_size=14)
        button.bind(on_press=map_screen)
        button2 = Button(text='Arena', font_size=14)
        button2.bind(on_press=arena_screen)

        layout.add_widget(button)
        layout.add_widget(button2)

        return layout


class Treasure_HuntApp(App):
    def build(self):
        # Initialise screens with names as identifiers
        screen1 = Screen(name='menuscreen')
        screen2 = Screen(name='mapgen')
        screen3 = Screen(name='arenascreen')

        #access to arena screen
        arena_screen = arena.Arena_Main()
        arena_layout = arena_screen.start_arena()

        # Access to the menu screen
        menu = MenuCore()
        menu_layout = menu.menu_screen_layout()

        # Create objects of program sections
        core = map_gen.MapGenCore()
        map_layout = core.block_gen()
        btn_layout = core.side_buttons()

        # map_gen_layout holds both parts of the Map Gen UI
        map_gen_layout = GridLayout(cols=2)
        map_gen_layout.add_widget(map_layout)
        map_gen_layout.add_widget(btn_layout)

        # Adds layouts to the screen manager as screen
        screen1.add_widget(menu_layout)
        screen2.add_widget(map_gen_layout)
        screen3.add_widget(arena_layout)

        # Sequentially adds screens to the screen manager
        sm.add_widget(screen1)
        sm.add_widget(screen2)
        sm.add_widget(screen3)
        return sm


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Treasure_HuntApp().run()