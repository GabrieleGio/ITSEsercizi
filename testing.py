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
