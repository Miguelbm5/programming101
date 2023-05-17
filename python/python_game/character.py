
# Provides the template for all the characters, heroes or enemies
from typing import Dict


class Character:
    def __init__(self, name: str, max_hp: int, max_mp: int, strength: int, defense: int, magic: int, magic_defense: int):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.max_mp = max_mp
        self.mp = max_mp
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.magic_defense = magic_defense
        self.special = NotImplemented
        self.special_cost = NotImplemented

    def receive_damage(self, damage: int):
        pass

    # def receive_magic_damage(self, damage: int):
    #     pass

    # def heal(self, recover_pts: int):
    #     pass

    # def recover_mp(self, recover_mp: int):
    #     pass

    # def execute_special(self, my_party: Dict[str, "Character"] = None, adversaries: Dict[str, "Character"] = None):
    #     # This function must be implemented by each children
    #     raise NotImplemented
