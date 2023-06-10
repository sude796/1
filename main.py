import random

class Auction:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def show_items(self):
        print("Items in the auction:")
        for item in self.items:
            print(item)

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pets = []
        self.furniture = []

    def buy_pet(self, pet):
        if self.money >= pet.price:
            self.pets.append(pet)
            self.money -= pet.price
            print(f"Bought a {pet.species} named {pet.name} for {pet.price} dollars.")
        else:
            print(f"Not enough money to buy the {pet.species}.")

    def buy_furniture(self, furniture):
        if self.money >= furniture.price:
            self.furniture.append(furniture)
            self.money -= furniture.price
            print(f"Bought {furniture.name} for {furniture.price} dollars.")
        else:
            print(f"Not enough money to buy {furniture.name}.")

    def sell_car(self, auction):
        if self.car is None:
            print("You don't have a car to sell.")
            return

        auction.offer(self.car)
        self.car = None
        print("Your car has been put up for auction.")

    def buy_car(self, auction):
        if self.car is not None:
            print("You already have a car.")
            return

        car = auction.buy()
        if car is not None:
            self.car = car
            self.money -= car.price
            print(f"You bought a {car.brand} for {car.price} dollars.")
        else:
            print("There are no cars available for purchase at the auction.")

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job} with a salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)

        if self.satiety < 20:
            print('I`ll go eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('I want to chill, but there is so much mess... \n So I will clean the house')
                self.clean_home()
            else:
                print('Let`s chill')
                self.chill()
        elif self.money < 0:
            print('Start working')
            self.work()
        elif self.car.strength < 15:
            print('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            print('Let`s chill')
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('Cleaning time')
            self.clean_home()
        elif dice == 4:
            print('Time for treats!')
            self.shopping(manage='delicacies')


        if self.gladness < 10:
            self.visit_doctor()
        elif self.satiety < 10:
            self.self_medicate()

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('I bought delicacies')
            self.money -= 15
            self.gladness += 10
            self.satiety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"fuel - {self.car.fuel}")
        print(f"strength - {self.car.strength}")

    def visit_doctor(self):
        print("I'm feeling unwell. Time to visit the doctor!")
        self.money -= 200
        self.gladness += 5
        self.satiety -= 2

    def self_medicate(self):
        print("I'm feeling unwell. Time for some self-medication!")
        self.money -= 50
        self.gladness += 3
        self.satiety -= 2

    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False

    def sell_car(self):
        if self.car is not None:
            auction_price = random.randint(1000, 10000)
            print(f"Selling {self.car.brand} car on the auction for {auction_price} dollars.")
            self.money += auction_price
            self.car = None
        else:
            print("You don't have a car to sell.")

    def buy_car(self):
        if self.car is None:
            auction_price = random.randint(1000, 10000)
            if self.money >= auction_price:
                car = Auto(brands_of_car)
                self.car = car
                self.money -= auction_price
                print(f"Bought a {self.car.brand} car on the auction for {auction_price} dollars.")
            else:
                print("Not enough money to buy a car.")
        else:
            print("You already have a car.")

    def sell_house(self):
        if self.home is not None:
            auction_price = random.randint(10000, 50000)
            print(f"Selling the house on the auction for {auction_price} dollars.")
            self.money += auction_price
            self.home = None
        else:
            print("You don't have a house to sell.")

    def buy_house(self):
        if self.home is None:
            auction_price = random.randint(10000, 50000)
            if self.money >= auction_price:
                house = House()
                self.home = house
                self.money -= auction_price
                print(f"Bought a house on the auction for {auction_price} dollars.")
            else:
                print("Not enough money to buy a house.")
        else:
            print("You already have a house.")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


class Pet:
    def __init__(self, species, name, price):
        self.species = species
        self.name = name
        self.price = price


class Furniture:
    def __init__(self, name, price):
        self.name = name
        self.price = price


job_list = {
    'Java developer': {'salary': 3000, 'gladness_less': 15},
    'Python developer': {'salary': 4000, 'gladness_less': 20},
    'Web designer': {'salary': 2500, 'gladness_less': 10},
    'Data analyst': {'salary': 3500, 'gladness_less': 12},
    'Project manager': {'salary': 5000, 'gladness_less': 25}
}

pet_list = {
    'dog': {'price': 200},
    'cat': {'price': 100},
    'parrot': {'price': 50}
}

furniture_list = {
    'sofa': {'price': 500},
    'table': {'price': 300},
    'chair': {'price': 200},
    'bed': {'price': 800}
}

brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 10},
    'Mercedes': {'fuel': 100, 'strength': 100, 'consumption': 12},
    'Audi': {'fuel': 100, 'strength': 100, 'consumption': 15},
    'Toyota': {'fuel': 100, 'strength': 100, 'consumption': 8},
    'Honda': {'fuel': 100, 'strength': 100, 'consumption': 10},
}

auction = Auction()

human = Human()
for day in range(1, 11):
    human.live(day)
    print('\n')
