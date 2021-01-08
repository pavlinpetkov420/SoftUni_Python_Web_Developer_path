class Zoo:
    # Total animals counter
    __animals = 0

    # initialization for needed attributes
    def __init__(self, name, mammals=None, fish=None, birds=None):
        self.name = name
        self.mammals = mammals or []
        self.fish = fish or []
        self.birds = birds or []

    # add animals method, distribution to species list
    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        else:
            self.birds.append(name)
        Zoo.__animals += 1

    # get info method, return info about needed species and total count of animals in the zoo
    def get_info(self, species):
        result = ""
        if species == 'mammal':
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result += f"Fishes in {self.name}: {', '.join(self.fish)}\n"
        else:
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


# creating new object
new_zoo = Zoo(input())
input_counts = int(input())

# collecting user data transfer
for x in range(input_counts):
    raw_data = input().split()
    type_animal = raw_data[0]
    name_animal = raw_data[1]

    new_zoo.add_animal(type_animal, name_animal)

needed_species_info = input()
print(new_zoo.get_info(needed_species_info))
