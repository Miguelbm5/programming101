
import hero
from character import Character
from typing import Dict


class Warrior(hero.Hero):
    def __init__(self, name: str):
        super().__init__(name, max_hp=100, max_mp=10,
                         strength=20, defense=20, magic_defense=0, magic=0)
        self.special = "round slash"
        self.special_cost = 3

    def level_up(self):
        self.max_hp = int(self.max_hp * 1.2)
        self.strength = int(self.strength * 1.1)
        self.defense = int(self.defense * 1.1)
        self.max_mp = self.max_mp + 1
        self.hp = self.max_hp
        self.mp = self.max_mp

    def execute_special(self, my_party: Dict[str, Character] = None, adversaries: Dict[str, Character] = None):
        if self.mp < self.special_cost:
            print(f"{self.name} doesn't have enough magic to execute {self.special}")
            return
        self.mp = self.mp - self.special_cost

        print(f"{self.name} executes {self.special}, damaging all enemies")
        for a in adversaries:
            adversaries[a].receive_damage(self.strength)
