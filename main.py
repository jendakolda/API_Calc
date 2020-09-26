# This is a sample Python script.
from dearpygui.dearpygui import *
from dearpygui.wrappers import *


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def retrieve_values(sender, data):
    set_value("##inputtext", str(get_value("Input Float##widget")))
    set_value("##labeltext", str(get_value("Input Float##widget")))


def applyTextMultiplier(sender, data):
    fontMultiplier = get_value("Font Size Multiplier")
    set_global_font_scale(fontMultiplier)


def applyTheme(sender, data):
    theme = get_value("Themes")
    set_theme(theme)


class API_Calc(object):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    set_main_window_size(800, 800)
    set_theme('Dark 2')
    themes = ["Dark", "Light", "Classic", "Dark 2", "Grey", "Dark Grey", "Cherry", "Purple", "Gold", "Red"]
    add_combo("Themes", themes, default_value="Dark", callback=applyTheme)

    add_slider_float("Font Size Multiplier", default_value=1.0, min_value=0.0, max_value=2.0,
                     callback=applyTextMultiplier)
    with tab_bar(name='tab_bar_1'):
        with tab(name='tab1'):
            add_indent(offset=30)
            add_text('Pokus o zadani cisla')
            add_indent(offset=50)
            add_text('Zadat cislo')
            add_same_line(spacing=100)
            add_input_float("Input Float##widget", default_value=0, width=75, tip='Zadej cislo',
                            callback=retrieve_values, on_enter=True)
            # unindent()
            add_text('Zadane cislo je')
            add_same_line(spacing=100)
            add_text('vysledek', callback_data='Input Float##widget')
            add_input_text("##inputtext", readonly=True, default_value="0", width=75)
            add_label_text('##labeltext', data_source='##inputtext', value='')

        with tab(name='tab2'):
            add_text('tohle je tab 2')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    API_Calc()
    start_dearpygui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
