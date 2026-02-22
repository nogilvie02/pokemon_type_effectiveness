# type_effectiveness
import json
from pokemon_types import PokemonType


# type chart inputs defensive type as key, then returns dict of all attacking types not neutral
# Ex: Bulbasaur type1 = Grass, type2 = Poison
# Grass dict -> "Fire": 2x, "Water": 0.5x, ..., "Bug": 2x.
# Poison dict -> ...
def load_type_chart():
    with open("types.json", "r") as file:
        return json.load(file)
    

def get_type_dict(type1, type2 = None):
    type_chart = load_type_chart()
    if not type2:
        return type_chart[type1]
    # todo: type2 as well as type1

