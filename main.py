# This is a sample Python script.
from modules import gui

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    API = gui.GuiBuilder()
    API.make_gui()
    API.run_gui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# TODO implement saving / export
# TODO Implement OOP Callbacks

# from dearpygui.core import *
#
#
# class Entity:
#     def __init__(self):
#         pass
#
#     def do_something(self, *args):
#         print("See?", args)
#
#     def do_another(self, *args):
#         print("What?", args)
#
#
# def oop_callback(instance_method):
#     def cb(*args):
#         return instance_method(instance_method.__self__, *args)
#
#     return cb
#
#
# ent = Entity()
# add_button("See me", callback=oop_callback(ent.do_something))
# add_button("Watch me", callback=oop_callback(ent.do_another))
# start_dearpygui()
