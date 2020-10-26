from dearpygui.core import *
from dearpygui.simple import *
from dearpygui.demo import *

with window(name='win'):
    show_documentation()

    show_demo()

start_dearpygui(primary_window='win')


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
# add_button("See me", callback=oop_callback(Entity().do_something))
# add_button("Watch me", callback=oop_callback(ent.do_another))
# start_dearpygui()


