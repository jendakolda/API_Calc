# This is a sample Python script.
from dearpygui.dearpygui import *
from dearpygui.wrappers import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def retrieve_values(sender, data):
    set_value("##inputtext", str(get_value("Input Float##widget")))
    set_value("##labeltext", str(get_value("Input Float##widget")))


def formula_show(sender, data):
    with window('Formula for Steam PRV Sizing', autosize=True, resizable=False,
                movable=True, title_bar=True, on_close=on_formula_close):
        add_image('formula_steam', "pictures\API520_A_Steam.png")
        # end()


def on_formula_close(sender, data):
    delete_item(sender)


def clear_fields(self, sender, data):
    pass


def export_results(sender, data):
    pass


class API_Calc(object):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.

    def __init__(self):
        set_main_window_size(width=1000, height=1000)
        set_theme('Light')

        with menu_bar(name='Main Menu'):
            with menu(name='File'):
                add_menu_item('Save')
                add_menu_item('item 2')
            with menu(name='Settings'):
                with menu('Theme'):
                    add_menu_item('Theme 1')
                    add_menu_item('Theme 2')

    with tab_bar(name='tab_bar_1'):
        #     with tab(name='Gas/Vapor##tab1'):
        #         add_indent(offset=30)
        #         add_text('Pokus o zadani cisla')
        #         add_indent(offset=50)
        #         add_text('Zadat cislo')
        #         add_same_line(spacing=100)
        #         add_input_float("Input Float##widget", default_value=0, width=75, tip='Zadej cislo',
        #                         callback=retrieve_values, on_enter=True)
        #         # unindent()
        #         add_text('Zadane cislo je')
        #         add_same_line(spacing=100)
        #         add_text('vysledek', callback_data='Input Float##widget')
        #         add_input_text("##inputtext", readonly=True, default_value="0", width=75)
        #         add_label_text('##labeltext', data_source='##inputtext', value='')

        with tab(name='Steam##tab2'):
            # lists of data on tab 2:
            tab2_inputs = ["##valve_tag"]

            with group('2heading'):
                add_spacing(count=2)
                add_text(
                    'Calculates required relief valve area for an API 520 valve passing a steam\n'
                    ' - at either saturation or superheat but not partially condensed.')
                add_spacing(count=2)
                add_indent(offset=20)
                add_button("Show Formula", callback=formula_show)
                add_same_line(spacing=20)
                add_button("Clear All", callback=clear_fields)
                add_same_line(spacing=20)
                add_button("Export Results", callback=export_results)
                unindent()
                add_spacing(count=2)
                add_separator()
            with group('##2input_widgets', tip='Input data for Steam relieve calculation'):
                add_spacing(count=5)

                add_indent(offset=20)
                add_text('Valve Tag:')
                add_same_line(spacing=10)
                add_input_text("##valve_tag", default_value='PSV', uppercase=True, no_spaces=True, width=100,
                               tip='Name of the valve')
                add_spacing(count=5)
                unindent()

                add_indent(offset=5)
                add_text('m  =')
                add_same_line(spacing=10)
                add_input_float("kg / s, Mass flow rate of steam through the valve.##2widget1", default_value=0,
                                width=75, tip='Zadej cislo',
                                callback=retrieve_values, on_enter=True)

                add_text('T  =')
                add_same_line(spacing=10)
                add_input_float("K, Temperature of steam entering the valve.##2widget2",
                                default_value=273.15, width=75, tip='Zadej cislo',
                                callback=retrieve_values, on_enter=True)

                add_text('P1 =')
                add_same_line(spacing=10)
                add_input_float(
                    "Pa, Upstream relieving pressure; set pressure + allowable overpressure + atm. pressure.##2widget3",
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

        with tab(name='Liquid##tab3'):
            add_text('tohle je tab 3')

        with tab(name='Two-Phase##tab4'):
            add_text('tohle je tab 4')

        with tab(name='Rupture Disk##tab5'):
            add_text('tohle je tab 5')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    API_Calc()
    start_dearpygui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
