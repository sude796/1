import random


# class Student:
#     amount_of_students = 0
#
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students += 1
#
#
# roman = Student()
# maria = Student(height=50)
# maria1 = Student(height=10)
# print(roman.height)
# print(maria.height)
# print(roman.amount_of_students,'Roman')
# print(Student.amount_of_students,'Students')

# class Student:
#     def __init__(self):
#         self.height += 10
#     height = 160
#     def printer(self):
#         print(self.height)
#
#
# roman = Student()
# roman1 = Student()
# roman2 = Student()
#
# roman.printer()


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally...')

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life."
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


vasya = Student(name='Vasya')

for day in range(365):
    if vasya.alive == False:
        break
    vasya.live(day)