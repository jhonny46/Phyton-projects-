class Dog:
    def __init__(self):
        self.tempermant = "Loyal"

    def bark(self):
        print("Woof, woof!")
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "friendly"


labrador = Labrador()

print(labrador.temperament)

Example 2


class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")