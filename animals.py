class Animal:
    '''This is the start of the animal class for 3120.'''

    def __init__(self, animal, species): 
        '''I removed kingdom as a parameter since every animal is in the Animalia kingdom'''
        self.animal = animal
        self.kingdom = 'animalia'
        self.species = species

    def describe(self):
        '''This will print a descriptive sentence about the animal.'''
        return f"{self.animal} is a species of {self.species} in the kingdom {self.kingdom}."

# Testing the describe method
elephant = Animal("The "+"Elephant", "Loxodonta africana")
print(elephant.describe())
