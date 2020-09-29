from dearpygui.core import *


class CreateGui:
    def __init__(self):
        self.theme = 'Light'
        self.width = 200
        self.height = 200

    class Menu:

        @staticmethod
        def print_stuff(sender, data):
            set_value('##output', 'nazdar')

        add_button('Ahoj', callback=print_stuff)
        add_label_text('##output')

    def make_gui(self):
        set_main_window_size(self.width, self.height)
        set_theme(self.theme)
        CreateGui.Menu()
        start_dearpygui()


API = CreateGui().make_gui()
