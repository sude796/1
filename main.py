import random


class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.hunger = random.randint(0, 10)  # від 0 до 10
        self.happiness = random.randint(0, 10)  # від 0 до 10

    def __str__(self):
        return f"{self.name} ({self.animal_type}) [Hunger: {self.hunger}, Happiness: {self.happiness}]"

    def play(self):
        self.hunger += 1
        self.happiness += 2
        print(f"{self.name} is playing.")

    def feed(self):
        self.hunger -= 2
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 1
        print(f"{self.name} is fed.")

    def wait(self):
        self.hunger += 1
        self.happiness -= 1
        print(f"{self.name} is waiting.")

    def is_hungry(self):
        return self.hunger > 5

    def is_unhappy(self):
        return self.happiness < 5


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")

    def meow(self):
        print("Meow!")
        self.happiness += 1


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")

    def bark(self):
        print("Woof!")
        self.happiness += 1
