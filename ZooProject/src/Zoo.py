class Zoo:
    fences_area = {}
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

    def add_guardian(self, guardian):
        if type(guardian) == ZooKeeper:
                if guardian not in self.zoo_keepers:
                    self.zoo_keepers.append(guardian)
                else:
                    print("Errore, guardiano già presente")
        else:
            print(f"Errore, formato del parametro sbagliato, {type(guardian)} non è uno Zoo Keeper")

    def add_fance(self, fence):
        if type(fence) == Fence:
            if fence not in self.fences:
                self.fences.append(fence)
                self.fences_area[fence.habitat] = fence.current_area
        else:
            print(f"Errore, formato del parametro sbagliato, {type(fence)} non è un recinto")

    @staticmethod
    def get_fences_area(habitat):
        return Zoo.fences_area[habitat]
    
    @staticmethod
    def set_fences_area(habitat, area):
        Zoo.fences_area[habitat] = area

    
    def describe_zoo(self):
        zoo_str = "Zoo:\n"
        if len(self.zoo_keepers) >=0:
            zoo_str += f"Guardians:\n\n"
            for guardian in self.zoo_keepers:
                zoo_str += f"ZooKeeper(name={guardian.name}, surname={guardian.surname}, id={guardian.id})\n\n"
        if len(self.fences) >= 0:
            zoo_str += f"Fences:\n\n"
            for recinto in self.fences:
                if len(recinto.animals) > 0:
                    zoo_str += f"Fence(area={recinto.area}, temperature={recinto.area}, habitat={recinto.habitat})\n\n"
                    zoo_str += f"with animals:\n\n"
                    for animal in recinto.animals:
                        zoo_str += f"Animal(name={animal.name}, species={animal.species}, age={animal.age})\n\n"
                zoo_str += '#'*30 + '\n\n'
        print(zoo_str)

            



class Animal:
    def __init__(self,name,species,age,height,width,preferred_habitat):
        if isinstance(name, str) and isinstance(species, str) and isinstance(age, int) and isinstance(height, (int, float)) and isinstance(preferred_habitat, str):
            if width > 0:
                self.name = name
                self.species = species
                self.age = age
                self.height = height
                self.width = width
                self.preferred_habitat = preferred_habitat
                self.health = round(100 * (1 / age), 3)
                self.nome_recinto = ""
            else: 
                raise TypeError("Errore, il parametro width della classe Animal deve essere positivo")
        else:
            raise TypeError("Errore tipo dei dati non corretto per la classe Animal")
    


class Fence:
    def __init__(self, area, temperature, habitat, animals=None):
        if isinstance(area, (int, float)) and isinstance(temperature, (int, float)) and isinstance(habitat, str):
            self.area = area
            self.temperature = temperature
            self.habitat = habitat
            if animals is None:
                self.animals = []
            else:
                self.animals = animals
            self.current_area = area
            self.vuoto = True
        else:
            raise TypeError("Errore tipo dei dati non corretto per la classe Fence")

    
class ZooKeeper:
    def __init__(self,name,surname,id):
        if isinstance(name, str) and isinstance(surname, str) and isinstance(id, int):
            self.name = name
            self.surname = surname
            self.id = id
        else:
            raise TypeError("Errore tipo dei dati non corretto per la classe ZooKeeper")
    
    def add_animal(self, animal: Animal, fence: Fence):
        if animal not in fence.animals:
            if fence.current_area >= animal.width:
                if animal.preferred_habitat == fence.habitat:
                    fence.animals.append(animal)
                    fence.current_area = fence.current_area - animal.width
                    Zoo.set_fences_area(fence.habitat, fence.current_area)
                    animal.nome_recinto = fence.habitat
                    fence.vuoto = False
                    print(f"{animal.name} aggiunto correttamente a {fence.habitat}, area del recinto rimanente: {Zoo.get_fences_area(fence.habitat)}")
                else:
                    print(f"Habitat sbagliato per {animal.name}")
            else:
                print(f"Spazio nel recinto insufficiente per aggiungere {animal.name}")
        else:
            print(f"L'animale {animal.name} è già presente nel recinto")

    
    
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals and animal.nome_recinto != "":
            fence.animals.remove(animal)
            fence.current_area = fence.current_area + animal.width
            animal.nome_recinto = ""
            print(f"{animal.name} rimosso/a da {fence.habitat}, nuova area del recinto: {fence.current_area}")
        else:
            print(f"Impossibile rimuovere {animal.name} perchè non è in un recinto")

        if fence.animals == []:
            fence.vuoto = True

    def feed(self, animal: Animal):
        if animal.nome_recinto != "":
            if animal.width * 1.02 <= Zoo.get_fences_area(animal.preferred_habitat):
                animal.health = animal.health * 1.01
                animal.width = animal.width * 1.02
                animal.height = animal.height * 1.02
                Zoo.set_fences_area(animal.preferred_habitat, Zoo.get_fences_area(animal.preferred_habitat) - (animal.width * 1.02 - animal.width))
                print(f'{animal.name} nutrito/a correttamente, salute attuale: {animal.health}, larghezza attuale: {animal.width}\n')
                print(f'Area del recinto rimanente: {Zoo.get_fences_area(animal.preferred_habitat)}')
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
            Zoo.set_fences_area(fence.habitat, fence.area)
            print(f"{fence.habitat} pulita correttamente in {tempopulizia} secondi, area disponibile: {fence.area}")
        else:
            print(f'Il recinto {fence.habitat} è già vuoto')
    