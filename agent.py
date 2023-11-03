import random

class Agent:
    """Creates an agent object with agent attributes and eats"""
    def __init__(self, wealth=0, metabolism=1, vision=1, age=0, max_age=10):
        self.wealth = wealth
        self.metabolism = metabolism
        self.age = age
        self.max_age = max_age
        self.vision = vision
        self.last_birth = 0
        self.children = []

    # Agents eat sugar, add to wealth, then metabolismolize it
    def eat(self):
        sugar = random.randint(1, 4)
        sugar = self.vision * sugar
        self.wealth += sugar
        self.wealth -= self.metabolism

    # Agents age 1 step for each model tick
    def grow_age(self):
        self.age += 1
    
    def give_ubi(self, ubi):
        self.wealth += ubi

    def print_wealth(self):
        print("Turtle wealth is ", self.wealth)

    def print_age(self):
        print("Turtle age is ", self.age)
    
    def pass_wealth(self):
        if self.children:
            wealth_share = self.wealth / len(self.children)
            for child in self.children:
                child.wealth += wealth_share
            self.wealth = 0