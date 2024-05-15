class Zoo:
    def __init__(self, fences=None, zoo_keepers=None):
        if fences is None:
            self.fences = []
        else:
            self.fences = fences
        if zoo_keepers is None:
            self.zoo_keepers = []
        else:
            self.zoo_keepers = zoo_keepers

    def __str__(self):
        zoo_str = "Zoo:\n"
        for i, recinto in enumerate(self.fences):
            zoo_str += f"Recinto {i}:\n"
            for animale in recinto.animals:
                zoo_str += f"-{animale.name}\n"
        return zoo_str


    def describe_zoo():
        pass

class Animal:
    def __init__(self,name,species,age,height,width,preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.current_fence_area = None


class Fence:
    def __init__(self, area, temperature, habitat, animals=None):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        if animals is None:
            self.animals = []
        else:
            self.animals = animals
        self.current_area = area

class ZooKeeper:
    def __init__(self,nome,cognome,id):
        self.nome = nome
        self.cognome = cognome
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        animal.current_fence_area = fence.current_area
        if animal not in fence.animals:
            if fence.current_area >= animal.width:
                if animal.preferred_habitat == fence.habitat:
                    fence.animals.append(animal)
                    fence.current_area = fence.current_area - animal.width
                    animal.current_fence_area = fence.current_area
                    print(f"{animal.name} aggiunto correttamente a {fence.habitat}, area del recinto rimanente: {animal.current_fence_area}")
                else:
                    print(f"Habitat sbagliato per {animal.name}")
            else:
                print(f"Spazio nel recinto insufficiente per aggiungere {animal.name}")
        else:
            print(f"L'animale {animal.name} è già presente nel recinto")

    
    
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.current_area = fence.current_area + animal.width

    def feed(self, animal: Animal):
        if animal.width * 1.02 <= animal.current_fence_area:
            animal.health = animal.health * 1.01
            animal.width = animal.width * 1.02
        else:
            print(f'Impossibile dare da mangiare a {animal.name}, non entrerebbe nel recinto')

    def clean(self, fence: Fence):
        pass

################################# ERRORI CORRETTI (CANCELLARE ALLA FINE)########################################
"""
class Fence:
    def __init__(self,area,temperature,habitat,animals = []):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = animals
"""
################################## ZONA TEST (CANCELLARE ALLA FINE)#######################################
zoo1 = Zoo()
recinto1 = Fence(1000,35,"Savana")
recinto2 = Fence(2000,20,"Giungla")

######## !!! ########
zoo1.fences.append(recinto1)
zoo1.fences.append(recinto2)
######## !!! ########

tigre = Animal("Tigre","Panthera Tigris",3,110,30,"Savana")
scimmia = Animal("Scimmia","boh",4,50,10,"Giungla")
leone = Animal("Leone","Leonis",7,100,40,"Savana")
pinguino = Animal("Pinguino","Pingu",3,40,10,"Glaciale")
animalebig = Animal("Enorme","Enorme",9999,9999,9999,"Savana")
guardiano1 = ZooKeeper("Mario","Rossi",1312)
guardiano1.add_animal(tigre,recinto1)
guardiano1.add_animal(scimmia,recinto2)
guardiano1.add_animal(animalebig,recinto1)
print(zoo1)



