from dearpygui.core import *
from dearpygui.simple import *

from modules.gas import Gas
from modules.liquid import Liquid
from modules.steam import Steam


class Menu:

    def __init__(self, window):
        self.window = window

    @staticmethod
    def apply_theme(sender, data):
        theme = get_value("##Themes")
        set_theme(theme)

    @staticmethod
    def quit_program(sender, data):
        quit()

    def generate(self):
        with menu_bar(name='Main Menu', parent=self.window):
            with menu(name='File'):
                add_menu_item('New File')
                add_menu_item('Load...')
                add_separator()
                add_menu_item('Save')
                add_menu_item('Save as...')
                add_separator()
                add_menu_item('Quit', callback=self.quit_program)

            with menu(name='Settings'):
                with menu('Select Theme'):
                    themes = ["Dark", "Light", "Classic", "Dark 2", "Grey", "Dark Grey", "Cherry", "Purple", "Gold", "Red"]
                    add_combo("##Themes", items=themes, default_value="Light", callback=self.apply_theme)


class GuiBuilder:
    def __init__(self):
        self.theme = 'Light'
        self.width = 1000
        self.height = 600

    def make_gui(self):
        with window(name='Main Window'):
            set_main_window_size(self.width, self.height)
            set_main_window_title('PRV sizing acc. to API RP 520')
            set_theme(self.theme)
            Menu('Main Window').generate()
            add_tab_bar(name='tab_bar_1', parent='Main Window')
            Gas('tab_bar_1').generate()
            Steam('tab_bar_1').generate()
            Liquid('tab_bar_1').generate()

    @staticmethod
    def run_gui():
        start_dearpygui(primary_window='Main Window')
