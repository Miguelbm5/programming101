class dragonTestsLevelUp(unittest.TestCase):

    def test_on_level_up_max_hp_increases(self):
        dragon = dragon("jimmy")
        initial_hp = dragon.max_hp
        dragon.level_up()
        self.assertEqual(int(initial_hp * 1.2), dragon.max_hp,
                         'Max HP increase on level up')

    def test_on_level_up_max_mp_increases(self):
        dragon = dragon("jimmy")
        initial_mp = dragon.max_mp
        dragon.level_up()
        self.assertEqual(initial_mp + 1, warrior.max_mp,
                         'Max MP increase on level up')

    def test_on_level_up_strength_increases(self):
        warrior = Warrior("Conan")
        strenght = warrior.strength
        warrior.level_up()
        self.assertEqual(int(strenght * 1.1), warrior.strength,
                         'Strenght increase on level up')

    def test_on_level_up_defense_increases(self):
        warrior = Warrior("Conan")
        defense = warrior.defense
        warrior.level_up()
        self.assertEqual(int(defense * 1.1), warrior.defense,
                         'Defense increase on level up')

    def test_on_level_up_hp_is_restored(self):
        warrior = Warrior("Conan")
        warrior.hp = 1
        warrior.level_up()
        self.assertEqual(warrior.max_hp, warrior.hp,
                         'HP is restored on level up')

    def test_on_level_up_mp_is_restored(self):
        warrior = Warrior("Conan")
        warrior.mp = 1
        warrior.level_up()
        self.assertEqual(warrior.max_mp, warrior.mp,
                         'MP is restored on level up')


class WarriorTests(unittest.TestCase):

    def test_warrior_special_damages_all_enemies(self):
        dragon = dragon("jimmy")
        heroes = {
            "knight": Character(name="spike", max_hp=100, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0),
            "Skeleton2": Character(name="Skeleton2", max_hp=50, max_mp=0, strength=0, defense=0, magic=0, magic_defense=0)
        }
        dragon.execute_special(my_party=None, adversaries=heroes)

        self.assertEqual(heroes["knight"].max_hp -
                         dragon.strength, enemies["Skeleton1"].hp)
        self.assertEqual(heroes[""].max_hp -
                         warrior.strength, enemies["Skeleton2"].hp)