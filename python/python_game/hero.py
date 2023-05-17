
from character import Character

# Provides the template for all the heros
# You should not create a Hero object directly, but a sub-class


class Hero(Character):
    def __init__(self, name: str, max_hp: int, max_mp: int, strength: int, defense: int, magic: int, magic_defense: int):
        super().__init__(name=name, max_hp=max_hp, max_mp=max_mp, strength=strength,
                         defense=defense, magic=magic, magic_defense=magic_defense)

    def level_up(self):
        # implement on each children class what happens on level up
        # (for example, warriors may increase strenght, and wizards magic)
        raise NotImplemented
