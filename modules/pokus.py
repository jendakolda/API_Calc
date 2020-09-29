from dearpygui.core import *


class CreateGui:
    def __init__(self):
        self.theme = 'Light'
        self.width = 200
        self.height = 200

    def make_gui(self):
        set_main_window_size(self.width, self.height)
        set_theme(self.theme)
        Menu()

    @staticmethod
    def run_gui():
        start_dearpygui()


class Menu:

    def print_stuff(sender, data):
        set_value('##output', 'nazdar')

    add_button('Ahoj', callback=print_stuff)
    add_label_text('##output')


API = CreateGui()
API.make_gui()
API.run_gui()
