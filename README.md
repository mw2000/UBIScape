# TurtleScape
## Model Overview 
A lean implementation of SugarScape in Python, optimized for experimentation

For this project, I implemented a SugarScape model in Python. (You can find background on the project and the SugarScape model here: http://ccl.northwestern.edu/netlogo/models/Sugarscape1ImmediateGrowback ) 

SugarScape is an agent-based model (ABM) first presented by Epstein and Axtell (1996) in their seminal work, Growing Artificial Societies. In their original model, agents are placed randomly on a grid. In each tick, or step of the model, they look around for food, move to the grid square they can see with the most amount of food, and eat the food. In addition to this, each agent metabolismolizes food at a certain rate, and if they run out, they die. Through this model, agents are born, live, and die (whether from simulated starvation or from age). If the model is stable, it can run indefinitely. 

While it sounds simple, the results generated can be profound. For instance, in Growing Artificial Societies, Epstein and Axtell were able to model  income inequality as an emergent phenomenon from SugarScape. Even today, researchers use SugarScape to model a variety of population dynamics. As an example, included in this repository is a chapter from my dissertation titled "A Model of Giving", where I used SugarScape to model the impacts of charity, philanthropy, and preferences for charity in a simulated society. 

In fact, it was this research that motivated me to implement SugarScape in Python as an alternative to NetLogo's BehaviorSpace. Even though BehaviorSpace is an intuitive and effective way to run experiments on varying parameters of an agent-based model, it is not efficient, nor is the output in a format that is easy to analyze using statistical software. 

To address the issue of efficiency, I designed this implementation to keep only what is necessary to run experiments. Most notably, this implementation is lacking a GUI. While a GUI within an agent-based model can provide incredibly valuable insights, it eats up too much memory when running thousands of experiments. It is the intention of this project to provide a SugarScape implementation that is useful and efficient for research. Because reproducible experiments are so critical, efficiency and useful output is key.

In this implementation of SugarScape, the agents are naive. They look around for food, but the spacial aspects aren?t inherently needed. Therefore, I programmed agents to eat random amounts of sugar with a random metabolism (within a given user-defined range). I also simulated vision as a multiplier of sugar, which reproduces the more spacial vision aspects without the need for a GUI.

The birth and death rates in this TurtleScape simulation work in the same way as in the original SugarScape. Agents die when they run out of sugar or age out (with the maximum age being user defined). They are born into the model with a user-defined birth rate at each tick. Then, the output is
either the number of surviving turtles, total wealth, and average wealth per turtle. 

To build on this in future iterations, I plan to add calculations such as a GINI coefficient, and with output going beyond simple print statements. Specifically, I would like to go beyond the BehaviorSpace-style output. It?s in a very un-user friendly .csv format that has per tick data and per simulation data, without any formatting that allows it to be easily imported into statistical software. In fact typically it has taken me more time to clean and format the BehaviorSpace output than it does to actually design and run the experiments. Instead, my plan is to add the ability to let the user choose JSON as an option for the export.
max_age
## Model Instructions
First, use the following code in the command line:

```
!python turtlescape.py main
```

This will run the main program. If you want to see a stable model, input higher numbers for wealth, vision, maxage, and maxruns, and lower numbers for metabolism. If you want to see less variation in the model, choose shorter ranges. Larger ranges will yield larger variation in the model. These will be apparent in the model output. If you just want to see 1 run, enter in 1 for u_simulations. It can be easily tested with 5 simulations, but you can enter in 500 to see how it could be used for research. I suggest trying all of these to truly see the model?s capabilities.

As always, suggestions are both appreciated and welcome. 