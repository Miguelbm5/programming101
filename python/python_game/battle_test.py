import unittest
from battle import Battle
from character import Character


class Battletests(unittest.TestCase):
    pass

    # def test_a_battle_is_not_over_if_at_least_one_hero_and_one_enemy_have_hp(self):

    #     heroes = {
    #         "Pip": Character(name="Pip", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
    #         "Pop": Character(name="Pop", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
    #     }
    #     enemies = {
    #         "Skeleton1": Character(name="Skeleton1", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
    #         "Skeleton2": Character(name="Skeleton2", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
    #     }

    #     battle = Battle(heroes=heroes, enemies=enemies)
    #     self.assertFalse(battle.is_over(), "Heroes and enemies alive")

    #     # Test that its not over even if only one has hp
    #     heroes["Pip"].hp = 0
    #     enemies["Skeleton1"].hp = 0
    #     self.assertFalse(battle.is_over(), "One hero, one enemy alive")

    #     # Same, with the last payer and enemy
    #     heroes["Pip"].hp = 10
    #     enemies["Skeleton1"].hp = 10
    #     heroes["Pop"].hp = 0
    #     enemies["Skeleton2"].hp = 0
    #     self.assertFalse(battle.is_over(), "last hero, last enemy")

    # def test_a_battle_is_over_if_all_heroes_are_KO(self):
    #     heroes = {
    #         "Pip": Character(name="Pip", max_hp=0, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
    #         "Pop": Character(name="Pop", max_hp=0, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
    #     }
    #     enemies = {
    #         "Skeleton1": Character(name="Skeleton1", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
    #         "Skeleton2": Character(name="Skeleton2", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
    #     }

    #     battle = Battle(heroes=heroes, enemies=enemies)
    #     self.assertTrue(battle.is_over(), "All heroes KO")

    #     # Since the conditions are the same, assert that the battle is lost
    #     self.assertFalse(battle.is_won(), "Lost, heroes KO")

    # def test_a_battle_is_over_if_all_enemies_are_KO(self):
    #     heroes = {
    #         "Pip": Character(name="Pip", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
    #         "Pop": Character(name="Pop", max_hp=10, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
    #     }
    #     enemies = {
    #         "Skeleton1": Character(name="Skeleton1", max_hp=0, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
    #         "Skeleton2": Character(name="Skeleton2", max_hp=0, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
    #     }

    #     battle = Battle(heroes=heroes, enemies=enemies)
    #     self.assertTrue(battle.is_over(), "All enemies KO")

    #     # Since the conditions are the same, assert that the battle is won
    #     self.assertTrue(battle.is_won(), "Won, all enemies defeated")


# In many languages, the program entry point is called "main"
# In python, __name__ takes the name of the file, but if we're
# from this file, then it takes the name '__main__'
# In other words, the following code will not execute if we are importing
# the file
if __name__ == '__main__':
    unittest.main()
