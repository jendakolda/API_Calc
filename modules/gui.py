from dearpygui.core import *
from dearpygui.simple import *

from modules.gas import Gas
from modules.liquid import Liquid
from modules.steam import Steam


class Menu:

    def apply_theme(sender, data):
        theme = get_value("##Themes")
        set_theme(theme)

    with menu_bar(name='Main Menu'):
        with menu(name='File'):
            add_menu_item('Save')
            add_menu_item('item 2')
        with menu(name='Settings'):
            with menu('Select Theme'):
                themes = ["Dark", "Light", "Classic", "Dark 2", "Grey", "Dark Grey", "Cherry", "Purple", "Gold", "Red"]
                add_combo("##Themes", items=themes, default_value="Light", callback=apply_theme)


class Tabs:
    add_tab_bar(name='tab_bar_1')


class GuiBuilder:
    def __init__(self):
        self.theme = 'Light'
        self.width = 1000
        self.height = 600

    def make_gui(self):
        set_main_window_size(self.width, self.height)
        set_theme(self.theme)
        Menu()
        Tabs()
        Gas('tab_bar_1').generate()
        Steam('tab_bar_1').generate()
        Liquid('tab_bar_1').generate()

    @staticmethod
    def run_gui():
        start_dearpygui()
