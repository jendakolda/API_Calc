from dearpygui.core import *
from dearpygui.simple import *


def theme_setting(sender, data):
    set_theme(data)


def formula_show(sender, data):
    with window('Formula for Steam PRV Sizing', autosize=True, no_resize=True,
                no_move=False, no_title_bar=False, on_close=on_formula_close):
        add_image('formula_steam', "pictures\API520_A_Steam.png")


def on_formula_close(sender, data):
    delete_item(sender)


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
        Steam()
        Liquid()
        start_dearpygui()


class Menu:
    with menu_bar(name='Main Menu'):
        with menu(name='File'):
            add_menu_item('Save')
            add_menu_item('item 2')
        with menu(name='Settings'):
            with menu('Theme'):
                add_menu_item('Light##Theme 1', callback=theme_setting, callback_data='Light')
                add_menu_item('Dark##Theme 2', callback=theme_setting, callback_data='Dark')


class Tabs:
    with tab_bar(name='tab_bar_1'):
        pass


class Steam:
    @staticmethod
    def retrieve_values(sender, data):
        pass

    @staticmethod
    def clear_fields(sender, data):
        for i in data:
            set_value(i, 0)

    @staticmethod
    def export_results(sender, data):
        pass

    with tab(name='Steam##tab2', parent='tab_bar_1'):
        # lists of data on tab 2:
        tab2_inputs = ["##valve_tag",
                       "kg / s, Mass flow rate of steam through the valve.##2widget1",
                       "K, Temperature of steam entering the valve.##2widget2",
                       "Pa, Upstream relieving pressure; set pressure + allowable overpressure + atm. pressure.##2widget3",
                       ]

        with group('2heading'):
            add_spacing(count=2)
            add_text(
                'Calculates required relief valve area for an API 520 valve passing a steam\n'
                ' - at either saturation or superheat but not partially condensed.')
            add_spacing(count=2)
            add_indent(offset=20)
            add_button("Show Formula", callback=formula_show)
            add_same_line(spacing=20)
            add_button("Clear All", callback=clear_fields, callback_data=tab2_inputs)
            add_same_line(spacing=20)
            add_button("Export Results", callback=export_results)
            unindent()
            add_spacing(count=2)
            add_separator()
        with group('##2input_widgets', tip='Input data for Steam relieve calculation'):
            add_spacing(count=5)

            add_indent(offset=20)
            add_text('Valve Tag')
            add_same_line(spacing=10)
            add_input_text(tab2_inputs[0], default_value='PSV', uppercase=True, no_spaces=True, width=100,
                           tip='Name of the valve')
            add_spacing(count=5)
            unindent()

            add_indent(offset=5)
            add_text('m  =')
            add_same_line(spacing=10)
            add_input_float(tab2_inputs[1], default_value=0,
                            width=75, tip='Zadej cislo',
                            callback=retrieve_values, on_enter=True)

            add_text('T  =')
            add_same_line(spacing=10)
            add_input_float(tab2_inputs[2],
                            default_value=273.15, width=75, tip='Zadej cislo',
                            callback=retrieve_values, on_enter=True)

            add_text('P1 =')
            add_same_line(spacing=10)
            add_input_float(tab2_inputs[3],
                            default_value=101325, width=75, tip='Input pressure [Pa]',
                            callback=retrieve_values, on_enter=True)

            add_text('Kd =')
            add_same_line(spacing=10)
            add_input_float("[-], (Optional, default = 0.975) The effective discharge coefficient.##2widget4",
                            default_value=0.975, width=75, tip='Kd = (default = 0.975)',
                            callback=retrieve_values, on_enter=True)

            add_text('Kb =')
            add_same_line(spacing=10)
            add_input_float("[-], (Optional, default = 1) Correction due to vapor backpressure.##2widget5",
                            default_value=1, width=75, tip='Kb = (default = 1)',
                            callback=retrieve_values, on_enter=True)

            add_text('Kc =')
            add_same_line(spacing=10)
            add_input_float("[-], (Optional, default = 1) Combination correction factor"
                            " for installation with a rupture disk upstream of the PRV,##2widget6",
                            default_value=1, width=75, tip='Kc = (default = 1)',
                            callback=retrieve_values, on_enter=True)
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
