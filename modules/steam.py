from dearpygui.core import *
from dearpygui.simple import *

import modules.backend as be


class Steam:

    def __init__(self, tab_parent):
        # TODO transform output block to self.parameter
        self.parent = tab_parent
        self.input_txt = [
            "##valve_tag",
            "kg / h, Mass flow rate of steam through the valve.##2widget1",
            "°C, Temperature of steam entering the valve.##2widget2",
            "bar a, Upstream relieving pressure; set pressure + allowable overpressure + atm. pressure.##2widget3",
            "[-], (Optional, default = 0.975) The effective discharge coefficient.##2widget4",
            "[-], (Optional, default = 1) Correction due to vapor backpressure.##2widget5",
            "[-], (Optional, default = 1) Combination correction factor"
            " for installation with a rupture disk upstream of the PRV,##2widget6",
        ]
        self.input_def = ['PSV', 0, 0, 1.01325, 0.975, 1, 1]
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
        # TODO clear the output fields as well
        for i in range(len(self.input_txt)):
            set_value(self.input_txt[i], self.input_def[i])

    def calculate(self, sender, data):
        # TODO check the input data with popup window
        input_val = [get_value(self.input_txt[i]) for i, txt in enumerate(self.input_txt)]
        area, area_rounded, letter = be.steam_area(input_val[1:])
        set_value('m2, Minimum Required Area.', area)
        set_value('m2, Area rounded to API526 standard.', area_rounded)
        set_value('Area expressed as API526 letter.', letter)

    @staticmethod
    def export_results(sender, data):
        pass

    def generate(self):

        with tab(name='Steam##tab2', parent=self.parent):
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
                                width=75, tip='Mass flow to be relieved')

                add_text('T  =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[2],
                                default_value=self.input_def[2], width=75, tip='Relieving Temperature')

                add_text('P1 =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[3],
                                default_value=self.input_def[3], width=75, tip='Input pressure [Pa]')

                add_text('Kd =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[4],
                                default_value=self.input_def[4], width=75, tip='Kd = (default = 0.975)')

                add_text('Kb =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[5],
                                default_value=self.input_def[5], width=75, tip='Kb = (default = 1)')

                add_text('Kc =')
                add_same_line(spacing=10)
                add_input_float(self.input_txt[6],
                                default_value=self.input_def[6], width=75, tip='Kc = (default = 1)')
                unindent()
                add_separator()

            with group('##2output_widgets'):
                add_spacing(count=5)

                add_indent(offset=20)
                add_text('Sizing results:')
                add_same_line(spacing=10)
                add_button('Calculate!', callback=self.calculate, tip='Press to perform sizing calculations')
                add_spacing(count=5)
                unindent()

                add_indent(offset=5)
                add_text('A  =')
                add_same_line(spacing=10)
                add_input_text('m2, Minimum Required Area.', readonly=True,
                               default_value='', width=75, tip='Minimum Required Area.')
                add_text('Ar =')
                add_same_line(spacing=10)
                add_input_text('m2, Area rounded to API526 standard.', readonly=True,
                               default_value='', width=75, tip='Rounded acc. to API526')

                add_text('API526 Letter =')
                add_same_line(spacing=10)
                add_input_text('Area expressed as API526 letter.', readonly=True,
                               default_value='', width=75, tip='API526 letter')

                unindent()
                add_separator()
