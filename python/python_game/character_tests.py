import unittest
from character import Character



class CharacterHpTests(unittest.TestCase):
   

    def test_when_a_character_is_hit_its_hp_is_reduced(self):
        Character =Character(name="pip", max_hp=100, max_mp=0, stregnth=0,
                            defense=10, magic=0, magic_defense=0)

    def test_when_a_character_is_hit_its_hp_is_reduced(self):
        character = Character(name="Pip", max_hp=100, max_mp=0, strength=0,
                                defense=0, magic=0, magic_defense=0)

        self.assertEqual(character.hp, 100, "We initialized it to 100")
        character.receive_damage(50)
        self.assertEqual(character.hp, 50, "The hp should be reduced")

    def test_when_a_character_is_hit_the_defense_reduce_damage(self):
        character = Character(name="Pip", max_hp=100, max_mp=0, strength=0,
                                defense=10, magic=0, magic_defense=0)
        character.receive_damage(50)
        self.assertEqual(character.hp, 60, "Defense should reduce damage")
        if real_damage > 

    # def test_if_defense_is_greater_than_damage_there_should_be_no_damage(self):
    #     character = Character(name="Pip", max_hp=100, max_mp=0, strength=0,
    #                           defense=50, magic=0, magic_defense=0)
    #     character.receive_damage(50)
    #     self.assertEqual(character.hp, 100, "Equal defense, No damage")
    #     character.receive_damage(40)
    #     self.assertEqual(character.hp, 100, "Greater defense, No damage")

    # def test_hp_should_not_be_less_than_zero(self):
    #     character = Character(name="Pip", max_hp=10, max_mp=0, strength=0,
    #                           defense=0, magic=0, magic_defense=0)
    #     character.receive_damage(40)
    #     self.assertEqual(character.hp, 0, "K.O.")

    # def test_heal_should_recover_hp(self):
    #     character = Character(name="Pip", max_hp=100, max_mp=0, strength=0,
    #                           defense=0, magic=0, magic_defense=0)
    #     character.hp = 5
    #     character.heal(10)
    #     self.assertEqual(character.hp, 15, "Healed")

    # def test_recover_hp_should_not_go_beyond_max(self):
    #     character = Character(name="Pip", max_hp=100, max_mp=0, strength=0,
    #                           defense=0, magic=0, magic_defense=0)
    #     character.hp = 95
    #     character.heal(10)
    #     self.assertEqual(character.hp, 100, "Healed to max")


# class CharacterMpTests(unittest.TestCase):
#     def test_recover_mp_should_increase_mp(self):
#         character = Character(name="Pip", max_hp=100, max_mp=20, strength=0,
#                               defense=0, magic=0, magic_defense=0)
#         character.mp = 5
#         character.recover_mp(10)
#         self.assertEqual(character.hp, 15, "Recovered mp")

#     def test_recover_mp_should_not_go_beyond_max(self):
#         character = Character(name="Pip", max_hp=100, max_mp=20, strength=0,
#                               defense=0, magic=0, magic_defense=0)
#         character.hp = 15
#         character.heal(10)
#         self.assertEqual(character.hp, 20, "Recover mp to max")


# In many languages, the program entry point is called "main"
# In python, __name__ takes the name of the file, but if we're
# from this file, then it takes the name '__main__'
# In other words, the following code will not execute if we are importing
# the file
if __name__ == '__main__':
    unittest.main()
