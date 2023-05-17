from character import Character
from typing import Dict


class Battle:
    def __init__(self, heroes: Dict[str, Character], enemies: Dict[str, Character]):
        self.heroes = heroes
        self.enemies = enemies

    def is_over(self):
        pass

    def is_won(self):
        pass
