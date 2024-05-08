class Zoo:
    def __init__(self,fences=[],zoo_keepers=[]):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def __str__(self):
        print("Animali nel recinto:")
        for fence in self.fences:
            for animal in 



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
    def __init__(self,area,temperature,habitat,animals = []):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = animals

class ZooKeeper:
    def __init__(self,nome,cognome,id):
        self.nome = nome
        self.cognome = cognome
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        if animal not in self.animals:
            if animal.preferred_habitat == fence.habitat
            self.animals.append(animal)
    
    def remove_animal(self, animal: Animal, fence: Fence):
        pass

    def feed(self, animal: Animal):
        pass

    def clean(self, fence: Fence):
        pass


################################# ZONA TEST (CANCELLARE ALLA FINE)#######################################
fence = Fence()
tigre = Animal("Tigre","Panthera Tigris",3,110,30,"Savana",100)

