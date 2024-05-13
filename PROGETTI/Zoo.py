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

class Fence:
    def __init__(self, area, temperature, habitat, animals=None):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        if animals is None:
            self.animals = []
        else:
            self.animals = animals

class ZooKeeper:
    def __init__(self,nome,cognome,id):
        self.nome = nome
        self.cognome = cognome
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        if animal not in fence.animals:
            if fence.area >= animal.width:
                if animal.preferred_habitat == fence.habitat:
                    fence.animals.append(animal)
                    fence.area = fence.area - animal.width
    
    def add_fence(self, fence: Fence):
        if fence not in self.zoo.fences:
            self.zoo.add_fence(fence)
    
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area = fence.area + animal.width
        pass

    def feed(self, animal: Animal):
        pass

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
################################# ZONA TEST (CANCELLARE ALLA FINE)#######################################
zoo1 = Zoo()
recinto1 = Fence(1000,35,"Savana")
recinto2 = Fence(2000,20,"Giungla")

######## !!! ########
zoo1.fences.append(recinto1)
zoo1.fences.append(recinto2)
######## !!! ########

tigre = Animal("Tigre","Panthera Tigris",3,110,30,"Savana")
scimmia = Animal("Scimmia","boh",4,50,10,"Giungla")
guardiano1 = ZooKeeper("Mario","Rossi",1312)
guardiano1.add_animal(tigre,recinto1)
guardiano1.add_animal(scimmia,recinto2)
print(zoo1)
