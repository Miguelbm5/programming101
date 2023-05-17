
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplemented


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # This calls the __init__ of the parent (Animal)

    def make_sound(self):
        return "woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "meow"


class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "tweet"


class Mouse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "squeek"


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "moo"


class Frog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "croak"


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "toot"


class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "quack"


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "blub"


class Seal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "ow ow ow"


class Fox(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return '''Ring-ding-ding-ding-dingeringeding!
        Gering-ding-ding-ding-dingeringeding!
        Gering-ding-ding-ding-dingeringeding!'''


if __name__ == '__main__':
    animals = [Dog(""), Cat(""), Bird(""), Mouse(""), Cow(""), Frog(""), Elephant(""),
               Duck(""), Fish(""), Seal(""), Fox("")]

    for a in animals:
        print(f"{type(a).__name__} goes {a.make_sound()}")
