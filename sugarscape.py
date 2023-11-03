# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:10:41 2018

@author: marycboardman
"""
import random
import csv
import os
from agent import Agent
import matplotlib.pyplot as plt


class SugarScape(Agent):
    """Creates a list of agents and runs the model"""

    def __init__(self, agents=[], agent_wealth=[], wealth=0, metabolism=1,
                 vision=1, num_agent=1, age=0, max_age=10, birth=1,
                 maxruns=500, ubi=1, birthing_wealth=50):
        self.agents = []
        self.agent_wealth = []
        self.birth = birth
        self.maxruns = maxruns
        self.ubi = ubi
        self.current_year = 0
        self.birthing_wealth = birthing_wealth
        for a in range(num_agent):
            a = Agent(wealth, metabolism, vision, age, max_age)
            self.agents.append(a)

    # Represents each tick of the model. Has each agent eat, get older, and
    # kills off the ones with no wealth and/or too old through appending a
    # survivor list
    def year(self):  # Added 'tick' argument to track the current model tick
        survivors = []
        new_born = []  # List to hold new born agents
        for a in self.agents:
            a.eat()
            a.grow_age()
            a.give_ubi(self.ubi)
            if (a.wealth > 0) and (a.age < a.max_age):  # Modified max_age to max_age for consistency
                survivors.append(a)
            # Check conditions for birth
            if 20 <= a.age <= 40 and a.wealth >= self.birthing_wealth and (self.current_year - a.last_birth) >= 2:
                child = Agent()
                a.children.append(child)  # Update parent's children list
                a.last_birth = self.current_year
                new_born.append(child)
            # Pass wealth to children when the agent dies
            if a.age == a.max_age:
                a.pass_wealth()
        # Combine the lists of surviving and new born agents
        self.agents = survivors + new_born
        self.current_year += 1


    def write_to_csv(self):
        # Specify the name of the csv file
        file_name = 'run_data.csv'
        
        # Determine whether the file already exists (and thus has a header)
        file_exists = os.path.exists(file_name)
        
        # Open the csv file for appending
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Write the header row only if the file did not already exist
            if not file_exists:
                writer.writerow(['Year', 'Agent ID', 'Age', 'Wealth', 'Metabolism', 'Vision', 'Number of Children'])
            
            # Write a row for each agent
            for idx, agent in enumerate(self.agents):
                writer.writerow([self.current_year, idx, agent.age, agent.wealth, agent.metabolism, agent.vision, len(agent.children)])

    # Runs the model, feeds, ages, and kills the agents. Then adds agents
    # to the model according to birth. It then prints the output.
    def model(self):
        for i in range(self.maxruns):
            count = 0
            count += 1
            SugarScape.year(self)
            self.write_to_csv()  # Write data to csv at the end of each tick

        print("There are", len(self.agents), "agents")
        if len(self.agents) == 0:
            print("Oh no! Your agents are all dead!")
            print("They didn't even make it ", self.current_year, "runs!")
            print("Look at your dead agent!")
            print("\|     |/")
            print("---------O")
            print("\______/")
            pass
        else:
            agent_wealth = [a.wealth for a in self.agents]
            w = sum(agent_wealth)
            print("Total agent wealth is", w)
            a = (w/len(self.agents))
            print("Average agent wealth is", a, "units of sugar per agent.")
