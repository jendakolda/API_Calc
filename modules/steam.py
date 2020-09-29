from dearpygui.core import *
from dearpygui.simple import *


class Steam:

    def __init__(self, tab_parent):
        self.parent = tab_parent
        self.input_txt = [
            "##valve_tag",
            "kg / s, Mass flow rate of steam through the valve.##2widget1",
            "K, Temperature of steam entering the valve.##2widget2",
            "Pa, Upstream relieving pressure; set pressure + allowable overpressure + atm. pressure.##2widget3",
            "[-], (Optional, default = 0.975) The effective discharge coefficient.##2widget4",
            "[-], (Optional, default = 1) Correction due to vapor backpressure.##2widget5",
            "[-], (Optional, default = 1) Combination correction factor"
            " for installation with a rupture disk upstream of the PRV,##2widget6",
        ]
        self.input_def = ['PSV', 0, 273.15, 101325, 0.975, 1, 1]
        for i in range(len(self.input_txt)):
            add_data(self.input_txt[i], self.input_def[i])

    def formula_show(self, sender, data):
        with window('Formula for Steam PRV Sizing', autosize=True, no_resize=True,
                    no_move=False, no_title_bar=False, on_close=self.on_formula_close):
            add_image('formula_steam', "pictures\API520_A_Steam.png")

    @staticmethod
    def on_formula_close(sender, data):
        delete_item(sender)

    def clear_fields(self, sender, data):
        for i in range(len(self.input_txt)):
            set_value(self.input_txt[i], self.input_def[i])

    def retrieve_values(self, sender, data):
        input_val = [get_data(self.input_txt[i]) for i, txt in enumerate(self.input_txt)]
        print(input_val)

    @staticmethod
    def export_results(sender, data):
        pass

    def generate(self):

        with tab(name='Steam##tab2', parent=self.parent, before='Liquid##tab3'):
            with group('2heading'):
                add_spacing(count=2)
                add_text(
                    'Calculates required relief valve area for an API 520 valve passing a steam\n'
                    ' - at either saturation or superheat but not partially condensed.')
                add_spacing(count=2)
                add_indent(offset=20)
                add_button("Show Formula", callback=self.formula_show)
                add_same_line(spacing=20)
                add_button("Clear All", callback=self.clear_fields, callback_data=self.input_txt)
                add_same_line(spacing=20)
                add_button("Export Results", callback=self.export_results)
                unindent()
                add_spacing(count=2)
                add_separator()

            with group('##2input_widgets'):
                add_spacing(count=5)

                add_indent(offset=20)
                add_text('Valve Tag')
                add_same_line(spacing=10)
                add_input_text(self.input_txt[0], default_value=self.input_def[0], uppercase=True, no_spaces=True,
                               width=100,
                               tip='Name of the valve')
                add_spacing(count=5)
                unindent()

                add_indent(offset=5)
                add_text('m  =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[1], default_value=self.input_def[1],
                                width=75, tip='Mass flow to be relieved', on_enter=True)

                add_text('T  =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[2],
                                default_value=self.input_def[2], width=75, tip='Relieving Temperature', on_enter=True)

                add_text('P1 =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[3],
                                default_value=self.input_def[3], width=75, tip='Input pressure [Pa]', on_enter=True)

                add_text('Kd =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[4],
                                default_value=self.input_def[4], width=75, tip='Kd = (default = 0.975)', on_enter=True)

                add_text('Kb =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[5],
                                default_value=self.input_def[5], width=75, tip='Kb = (default = 1)', on_enter=True)

                add_text('Kc =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[6],
                                default_value=self.input_def[6], width=75, tip='Kc = (default = 1)', on_enter=True)
                unindent()
                add_separator()

            with group('##2output_widgets', tip='Output data for Steam relieve calculation'):
                add_spacing(count=5)

                add_indent(offset=20)
                add_text('Sizing results:')
                add_same_line(spacing=10)
                # add_input_text("##valve_tag", uppercase=True, no_spaces=True, width=100)
                add_spacing(count=5)
                unindent()
                add_button('Calculate!', callback=self.retrieve_values)
