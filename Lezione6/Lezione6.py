class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'Persona(name={self.name}, age={self.age})'


alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if bob.age >= alice.age:
    print(bob.age)
else:
    print(alice.age)

max = Person("Max K.", 25)
simon = Person("Simon G.", 48)
george = Person("George Z.", 25)

people = [alice,bob,max,simon,george]

youngestage = 200
youngestname = ""

for person in people:
    if person.age <= youngestage:
        youngestname = person.name
        youngestage = person.age


print(f"L'età più giovane è di {youngestname}, {youngestage} anni")
print(person)

print()
print()

class Student:
    def __init__(self,name,studyProgram):
        self.name = name
        self.studyProgram = studyProgram
        self.age = None
        self.gender = None

    def printInfo(self):
        return print(f"Il nome è {self.name}, l'età è {self.age} anni, il gender è {self.gender}, e il programma di studi è {self.studyProgram} ")
    
    def set_age(self, new_age):
        self.age = new_age

    def set_gender(self, new_gender):
        self.gender = new_gender
        
    
myself = Student("Gabriele","Cloud")
left_neighbour = Student("Marco","FullStack Developer")
right_neighbour = Student("Francesco","Cybersecurity")

myself.set_age(20)
myself.set_gender("Maschio")
myself.printInfo()

class Animal:
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
    
    