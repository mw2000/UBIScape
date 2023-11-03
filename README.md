# SugarScape
## Model Overview 
A lean implementation of SugarScape in Python, optimized for experimentation.

SugarScape is an agent-based model (ABM) first presented by Epstein and Axtell (1996) in their seminal work, Growing Artificial Societies. In their original model, agents are placed randomly on a grid. In each tick, or step of the model, they look around for food, move to the grid square they can see with the most amount of food, and eat the food. In addition to this, each agent metabolizes food at a certain rate, and if they run out, they die. Through this model, agents are born, live, and die (whether from simulated starvation or from age). If the model is stable, it can run indefinitely.

While it sounds simple, the results generated can be profound. For instance, in Growing Artificial Societies, Epstein and Axtell were able to model income inequality as an emergent phenomenon from SugarScape. Even today, researchers use SugarScape to model a variety of population dynamics. As an example, included in this repository is a chapter from my dissertation titled "A Model of Giving", where I used SugarScape to model the impacts of charity, philanthropy, and preferences for charity in a simulated society.

In fact, it was this research that motivated me to implement SugarScape in Python as an alternative to NetLogo's BehaviorSpace. Even though BehaviorSpace is an intuitive and effective way to run experiments on varying parameters of an agent-based model, it is not efficient, nor is the output in a format that is easy to analyze using statistical software.

To address the issue of efficiency, I designed this implementation to keep only what is necessary to run experiments. Most notably, this implementation is lacking a GUI. While a GUI within an agent-based model can provide incredibly valuable insights, it eats up too much memory when running thousands of experiments. It is the intention of this project to provide a SugarScape implementation that is useful and efficient for research. Because reproducible experiments are so critical, efficiency and useful output is key.

In this implementation of SugarScape, the agents are naive. They look around for food, but the spatial aspects aren’t inherently needed. Therefore, I programmed agents to eat random amounts of sugar with a random metabolism (within a given user-defined range). I also simulated vision as a multiplier of sugar, which reproduces the more spatial vision aspects without the need for a GUI.

The birth and death rates in this SugarScape simulation have been updated to allow for a more realistic representation of birth, including restrictions based on agent wealth, age, and frequency of birth, as well as inheritance of wealth upon the death of parent agents. 

The model now outputs data to a CSV file and also provides a visual representation of agent data using Matplotlib at the end of each simulation run. This allows for a more detailed analysis of the model's dynamics over time.

## Model Instructions
To run the model, use the following code in the command line:
```
python3 main.py
```
This will run the main program. You will be prompted to input model parameters via a JSON file. If you want to see a stable model, input higher numbers for wealth, vision, max_age, and max_runs, and lower numbers for metabolism. If you want to see less variation in the model, choose shorter ranges. Larger ranges will yield larger variation in the model. These will be apparent in the model output. 

At the end of each simulation run, a CSV file named `run_data.csv` will be generated containing data for each agent at each tick, and a scatter plot of agent wealth over time will be displayed.

As always, suggestions are both appreciated and welcome.
