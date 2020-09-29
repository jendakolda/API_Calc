# from dearpygui.core import *
# from dearpygui.simple import *
from modules.steam import *


class Menu:

    def theme_setting(sender, data):
        set_theme(data)

    with menu_bar(name='Main Menu'):
        with menu(name='File'):
            add_menu_item('Save')
            add_menu_item('item 2')
        with menu(name='Settings'):
            with menu('Theme'):
                add_menu_item('Light##Theme 1', callback=theme_setting, callback_data='Light')
                add_menu_item('Dark##Theme 2', callback=theme_setting, callback_data='Dark')


class Tabs:
    add_tab_bar(name='tab_bar_1')

    # with tab(name='Gas/Vapor##tab1'):
    #     add_text('tohle je tab 1')


class Liquid:
    with tab(name='Liquid##tab3', parent='tab_bar_1'):
        add_text('tohle je tab 3')
        #
        # with tab(name='Two-Phase##tab4'):
        #     add_text('tohle je tab 4')
        #
        # with tab(name='Rupture Disk##tab5'):
        #     add_text('tohle je tab 5')


class GuiBuilder:
    def __init__(self):
        self.theme = 'Light'
        self.width = 1000
        self.height = 1000

    def make_gui(self):
        set_main_window_size(self.width, self.height)
        set_theme(self.theme)
        Menu()
        Tabs()
        Steam('tab_bar_1').generate()
        Liquid()

    @staticmethod
    def run_gui():
        start_dearpygui()
