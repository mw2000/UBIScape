import json
from sugarscape import SugarScape
import random

def read_input_parameters(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Main method
def main():
    input_params = read_input_parameters("config.json")
    game = SugarScape(
        wealth=random.randint(input_params["min_wealth"], input_params["max_wealth"]),
        metabolism=random.randint(input_params["min_metabolism"], input_params["max_metabolism"]),
        vision=random.uniform(input_params["min_vision"], input_params["max_vision"]),
        num_agent=input_params["num_agent"],
        max_age=input_params["max_age"],
        birth=input_params["birth"],
        maxruns=input_params["max_runs"],
        ubi=input_params["ubi"]
    )
    for s in range(input_params["simulation"]):
        game.model()

# Initialization
if __name__ == "__main__":
    main()
