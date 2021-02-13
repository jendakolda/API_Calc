from dearpygui.core import *
from dearpygui.simple import *


class Gas:
    def __init__(self, tab_parent):
        # TODO transform output block to self.parameter
        self.parent = tab_parent
        self.input_var = []
        self.input_txt = []
        self.input_def = []
        self.input_tip = []

    def formula_show(self, sender, data):
        with window('Formula for Steam PRV Sizing', autosize=True, no_resize=True,
                    no_move=False, no_title_bar=False, on_close=self.on_formula_close):
            add_image('formula_gas', "pictures\API520_A_Steam.png")

    @staticmethod
    def on_formula_close(sender, data):
        delete_item(sender)

    def clear_fields(self, sender, data):
        # TODO clear the output fields as well
        for i in range(len(self.input_txt)):
            set_value(self.input_txt[i], self.input_def[i])

    @staticmethod
    def export_results(sender, data):
        pass

    def generate(self):
        with tab(name='Gas/Vapor##tab1', parent=self.parent):
            with group('1heading'):
                add_spacing(count=2)
                add_text('Calculates required relief valve area for an API 520 valve passing gas or vapor\n'
                         ' - at either critical or sub-critical conditions.')

                add_spacing(count=2)
                add_indent(offset=20)
                add_button("Show Formula##gas", callback=self.formula_show)
                add_same_line(spacing=20)
                add_button("Clear All##gas", callback=self.clear_fields, callback_data=self.input_txt)
                add_same_line(spacing=20)
                add_button("Export Results##gas", callback=self.export_results)
                unindent()
                add_spacing(count=2)
                add_separator()
