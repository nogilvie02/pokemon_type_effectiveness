# pokemon_types
from enum import Enum
import csv


class PokemonType(Enum):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    GRASS = "Grass"
    ELECTRIC = "Electric"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    STEEL = "Steel"
    DARK = "Dark"
    FAIRY = "Fairy"


class Pokemon():
    def __init__(self, name, type1, type2 = None):
        self.name = name
        self.type1 = type1
        self.type2 = type2


    def __repr__(self):
        if not self.type2:
            return f"{self.name} - type1: {self.type1}"
        return f"{self.name} - type1: {self.type1}, type2: {self.type2}"
    

def get_pokedex():
    pokedex = {}
    with open("pokemon_types.csv", "r") as file:
        reader = csv.reader(file)

    for row in reader:
        name = row[0]
        pokedex[name] = row[1:]
    return pokedex