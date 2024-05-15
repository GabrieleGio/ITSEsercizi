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
        self.nelrecinto = False


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
        self.vuoto = True

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
                    animal.nelrecinto = True
                    fence.vuoto = False
                    print(f"{animal.name} aggiunto correttamente a {fence.habitat}, area del recinto rimanente: {animal.current_fence_area}")
                else:
                    print(f"Habitat sbagliato per {animal.name}")
            else:
                print(f"Spazio nel recinto insufficiente per aggiungere {animal.name}")
        else:
            print(f"L'animale {animal.name} è già presente nel recinto")

    
    
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals and animal.nelrecinto == True:
            fence.animals.remove(animal)
            fence.current_area = fence.current_area + animal.width
            animal.nelrecinto = False
            print(f"{animal.name} rimosso/a da {fence.habitat}, nuova area del recinto: {fence.current_area}")
        else:
            print(f"Impossibile rimuovere {animal.name} perchè non è in un recinto")

        if fence.animals == []:
            fence.vuoto = True

    def feed(self, animal: Animal):
        if animal.nelrecinto == True:
            if animal.width * 1.02 <= animal.current_fence_area:
                animal.health = animal.health * 1.01
                animal.width = animal.width * 1.02
                animal.height = animal.height * 1.02
                animal.current_fence_area = animal.current_fence_area - (animal.width * 1.02 - animal.width)
                print(f'{animal.name} nutrito/a correttamente, salute attuale: {animal.health}, larghezza attuale: {animal.width}\n')
                print(f'Area del recinto rimanente: {animal.current_fence_area}')
            else:
                print(f'Impossibile dare da mangiare a {animal.name}, non entrerebbe nel recinto')
        else:
            print(f"Impossibile dare da mangiare a {animal.name} perchè non è nel recinto")

    def clean(self, fence: Fence):
        areaoccupata = 0
        tempopulizia = 100
        if fence.animals and fence.vuoto == False:
            if fence.current_area > 0:
                areaoccupata = fence.area - fence.current_area
                tempopulizia = areaoccupata / fence.current_area
            elif fence.current_area == 0:
                areaoccupata = fence.area - fence.current_area
                print(f"Area occupata: {areaoccupata}")
            fence.animals = []
            fence.vuoto = True
            fence.current_area = fence.area
            print(f"{fence.habitat} pulita correttamente in {tempopulizia} secondi, area disponibile: {fence.area}")
        else:
            print(f'Il recinto {fence.habitat} è già vuoto')


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
leone = Animal("Leone","Leonis",7,100,40,"Savana")
pinguino = Animal("Pinguino","Pingu",3,40,10,"Glaciale")
pantera = Animal("Pantera","Pantheras",5,100,100,"Savana")
animalebig = Animal("Enorme","Enorme",9999,9999,9999,"Savana")
animaleriempisavana = Animal("Fullsavana","Fullsavana",999,9999,1000,"Savana")
animaleriempigiungla = Animal("Fullgiungla","Fullgiungla",999,9999,2000,"Giungla")
guardiano1 = ZooKeeper("Mario","Rossi",1312)
guardiano1.add_animal(tigre,recinto1)
guardiano1.add_animal(scimmia,recinto2)
guardiano1.add_animal(animalebig,recinto1)
guardiano1.add_animal(leone,recinto1)
guardiano1.add_animal(pinguino,recinto2)
guardiano1.add_animal(pantera,recinto1)
guardiano1.feed(pantera)
guardiano1.feed(pantera)
print(zoo1)
guardiano1.clean(recinto1)
print(zoo1)
guardiano1.add_animal(tigre,recinto1)
guardiano1.add_animal(animalebig,recinto1)
guardiano1.add_animal(leone,recinto1)
guardiano1.feed(leone)
guardiano1.feed(leone)
print(zoo1)
guardiano1.remove_animal(leone,recinto1)
guardiano1.remove_animal(scimmia,recinto2)
guardiano1.feed(scimmia)
guardiano1.add_animal(scimmia,recinto2)
guardiano1.remove_animal(pinguino,recinto2)
print(zoo1)
guardiano1.clean(recinto1)
guardiano1.clean(recinto1)
print(zoo1)
guardiano1.add_animal(animaleriempisavana,recinto1)
print(zoo1)
guardiano1.clean(recinto1)
print(zoo1)
guardiano1.feed(scimmia)
guardiano1.add_animal(tigre,recinto1)
guardiano1.add_animal(leone,recinto1)
guardiano1.feed(tigre)
print(recinto1.vuoto)
print(recinto2.vuoto)