# class Grandparent:
#     def about(self):
#         print('I am Grandparent')
#
#     def about_myself(self):
#         print('I am Grandparent')
#
# class Parent(Grandparent):
#     def about_myself(self):
#         print('I am Parent')
#
# class Child(Parent):
#     def __init__(self):
#         super().about()
#         super().about_myself()
#
# vasya = Child()
#
#
#
# class Computer:
#     def calculate(self):
#         print('Calculating...')
#
# class Display:
#     def display(self):
#         print('I display the image on the screen...')
#
#
#
# class SmartPhone(Display, Computer):
#     pass
#
#
# iphone = SmartPhone()
#
# iphone.calculate()
# iphone.display()
# class Computer:
#     def __init__(self):
#         super().__init__()
#         self.memory = 128
#
# class Display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"
#
# class SmartPhone(Computer,Display):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
#
# iphone = SmartPhone()
#
# iphone.print_info()


class Computer:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__()
        self.memory = 128

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"

class SmartPhone(Computer,Display):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)


iphone = SmartPhone(model="Last")

iphone.print_info()