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
    def __init__(self,name,age,studyProgram):
        self.name = name
        self.age = age
        self.studyProgram = studyProgram

    def printInfo(self):
        return print(f"Il nome è {self.name}, l'età è {self.age} anni e il programma di studi è {self.studyProgram} ")
        
    
myself = Student("Gabriele",20,"Cloud")
left_neighbour = Student("Marco",22,"FullStack Developer")
right_neighbour = Student("Francesco",23,"Cybersecurity")

myself.printInfo()
myself.age = 25
    