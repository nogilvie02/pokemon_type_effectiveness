# pokemon_types
from enum import Enum


class PokemonType(Enum):
    NORMAL = "normal"
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"
    ICE = "ice"
    FIGHTING = "fighting"
    POISON = "poison"
    GROUND = "ground"
    FLYING = "flying"
    PSYCHIC = "psychic"
    BUG = "bug"
    ROCK = "rock"
    GHOST = "ghost"
    DRAGON = "dragon"
    STEEL = "steel"
    DARK = "dark"
    FAIRY = "fairy"
    

class Pokemon():
    def __init__(self, name, type1, type2 = None):
        self.name = name
        self.type1 = type1
        self.type2 = type2


    def __repr__(self):
        if not self.type2:
            return f"{self.name} - type1: {self.type1}"
        return f"{self.name} - type1: {self.type1}, type2: {self.type2}"
    