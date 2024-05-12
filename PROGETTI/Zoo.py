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
        zoo_str = "Zoo: \n"
        for i,recinto in enumerate(self.fences,1):
            zoo_str += f"Recinto {i}:\n"
            for animale in recinto.animals:
                zoo_str += f"-{animale.name}\n"
        return zoo_str


    def describe_zoo():
        pass

class Animal:
    def __init__(self,name,species,age,height,width,preferred_habitat,health):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = health

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
            if animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
    
    def remove_animal(self, animal: Animal, fence: Fence):
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
recinto1 = Fence(50,35,"Savana")
recinto2 = Fence(100,20,"Giungla")

######## !!! ########
zoo1.fences.append(recinto1)
zoo1.fences.append(recinto2)
######## !!! ########

tigre = Animal("Tigre","Panthera Tigris",3,110,30,"Savana",100)
scimmia = Animal("Scimmia","boh",4,50,10,"Giungla",100)
guardiano1 = ZooKeeper("Mario","Rossi",1312)
guardiano1.add_animal(tigre,recinto1)
guardiano1.add_animal(scimmia,recinto2)
print(zoo1.__str__())
