from dearpygui.core import *
from dearpygui.simple import *


class Liquid:

    def __init__(self, tab_parent):
        self.parent = tab_parent

    def generate(self):
        with tab(name='Liquid##tab3', parent=self.parent):
            add_text('tohle je tab 3')
