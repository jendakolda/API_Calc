# show_demo()
# show_documentation()
# start_dearpygui()


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

i = 0
star = 0
while i < 5:
    print('*')
    star += 1
    if i % 2 == 0:
        print('**')
        star += 2
    if i > 2:
        print('***')
        star += 3
    i = i + 1
print(star)
