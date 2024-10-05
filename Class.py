# Class Methods
class Dog:
    species = 'Canine'

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

dog1 = Dog('Buddy')
dog2 = Dog('Max')

print(dog1.species)  # Output: Canine
Dog.change_species('Feline')
print(dog2.species)  # Output: Feline
















