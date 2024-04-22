#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)



#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
name1 = "Mario"

# Lowercase
print(f"In lowercase: {name1.lower()}")

# Uppercase
print(f"In uppercase: {name1.upper()}")

# Title case
print(f"In title case: {name1.title()}")



#2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
#Your output should look something like the following,
#including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
famous_quote = "Steve Jobs once said, “Stay hungry, stay foolish.”"
print(famous_quote)



#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person.
#Then compose your message and represent it with a new variable called message. Print your message. 
famous_person = "Steve Jobs"
message = 'once said, "Stay hungry, stay foolish"'
print(f"{famous_person} {message}")



#2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
#Assign the value 'python_notes.txt' to a variable called filename. 
#Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
filename = "python_notes.txt"
filename_without_extension = filename.removesuffix(".txt")
print(filename_without_extension)



#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.
names = ['Alice', 'Bob', 'Charlie', 'Davide']
for name in names:
    print(name)



#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
#The text of each message should be the same, but each message should be personalized with the person’s name.
for name in names:
    print(f"E' un piacere vederti, {name}!")



#3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
#Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
mezzi_preferiti = ['auto', 'moto', 'bicicletta']

print(f"Mi piacerebbe possedere una bella {mezzi_preferiti[1]}.")
print(f"La mia {mezzi_preferiti[0]} è una Ford Focus")
print(f"Mi piace andare in {mezzi_preferiti[2]} nei giorni di sole.")



#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
#Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
guests = ['Kratos', 'Albert Einstein', 'Michael Jackson']

for guest in guests:
    print(f"Caro/a {guest.title()},\n\tSarebbe un onore per me averti come ospite a cena. Spero che tu possa accettare il mio invito.\nCordiali saluti,\nGabriele G.\n\n")



#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.
guests = ['Kratos', 'Albert Einstein', 'Michael Jackson']

for guest in guests:
    print(f"Caro/a {guest.title()},\n\tSarebbe un onore per me averti come ospite a cena. Spero che tu possa accettare il mio invito.\nCordiali saluti,\nGabriele G.\n\n")

print(f"Mi dispiace ma {guests[0].title()} non può più venire a cena.\n")

guests[0] = 'Atreus'

for guest in guests:
    print(f"Caro/a {guest.title()},\n\tSarebbe un onore per me averti come ospite a cena. Spero che tu possa accettare il mio invito.\nCordiali saluti,\nGabriele G.\n\n")



#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of invitation messages, one for each person in your list.
print("Ho trovato un tavolo più grande, quindi posso invitare più persone a cena!\n")

guests.insert(0, 'Mario Draghi')
guests.insert(len(guests) // 2, 'Alessandro Magno')
guests.append('Giulio Cesare')

for guest in guests:
    print(f"Caro/a {guest.title()},\n\tSarebbe un onore per me averti come ospite a cena. Spero che tu possa accettare il mio invito.\nCordiali saluti,\nGabriele G.\n\n")



#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
#• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
print("Mi dispiace, ma il mio nuovo tavolo da pranzo non arriverà in tempo per la cena.")
print("Purtroppo, posso invitare solo due persone per cena.\n")

while len(guests) > 2:
    guest = guests.pop()
    print(f"Caro/a {guest.title()},\n\tMi dispiace, ma purtroppo non posso invitarti a cena.\nCordiali saluti,\nGabriele G.")

for guest in guests:
    print(f"Caro/a {guest.title()},\n\tSono felice di invitarti ancora alla cena.\nCordiali saluti,\nGabriele G.")

del guests[:]
print(guests)



#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
#• Use sorted() to print your list in alphabetical order without modifying the actual list.
#• Show that your list is still in its original order by printing it.
#• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
#• Show that your list is still in its original order by printing it again.
#• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
#• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#• Use sort() to change your list so it’s stored in reverse-alphabetical order.
#Print the list to show that its order has changed.
places = ['Tokyo', 'Parigi', 'Rio de Janeiro', 'Sydney', 'Roma']

print("Lista originale:")
print(places)

print("\nOrdine alfabetico:")
print(sorted(places))

print("\nOrdine originale:")
print(places)

print("\nOrdine alfabetico al contrario:")
print(sorted(places, reverse=True))

print("\nOrdine originale:")
print(places)

print("\nAl contrario:")
places.reverse()
print(places)

print("\nOrdine originale:")
places.reverse()
print(places)

print("\nOrdine alfabetico:")
places.sort()
print(places)

print("\nOrdine alfabetico al contrario:")
places.sort(reverse=True)
print(places)



#3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
#use len() to print a message indicating the number of people you’re inviting to dinner.
num_guests = len(guests)
print(f'\nSto invitando {num_guests} persone per cena.\n')



#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
#Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
# Crea una lista di città
cities = ['Roma', 'Parigi', 'Londra', 'Madrid', 'Berlino']

# Usa len() per stampare il numero di città nella lista
print(f'Ci sono {len(cities)} città nella lista.')

# Usa sorted() per stampare la lista in ordine alfabetico
print('Le città in ordine alfabetico sono:')
print(sorted(cities))

# Usa reverse() per invertire l'ordine della lista
cities.reverse()
print('Le città in ordine inverso sono:')
print(cities)

# Usa append() per aggiungere una città alla fine della lista
cities.append('Barcellona')
print('La lista aggiornata è:')
print(cities)

# Usa insert() per aggiungere una città in una posizione specifica della lista
cities.insert(2, 'Amsterdam')
print('La lista aggiornata è:')
print(cities)

# Usa remove() per rimuovere una città dalla lista
cities.remove('Madrid')
print('La lista aggiornata è:')
print(cities)

# Usa pop() per rimuovere e restituire l'ultima città dalla lista
last_city = cities.pop()
print(f'L\'ultima città rimossa è: {last_city}')
print('La lista aggiornata è:')
print(cities)

# Usa index() per trovare l'indice di una città nella lista
index = cities.index('Parigi')
print(f'L\'indice di Parigi nella lista è: {index}')

# Usa count() per contare il numero di occorrenze di una città nella lista
count = cities.count('Roma')
print(f'Il numero di occorrenze di Roma nella lista è: {count}')

# Usa in per verificare se una città è presente nella lista
if 'Milano' in cities:
    print('Milano è presente nella lista.')
else:
    print('Milano non è presente nella lista.')

# Usa not in per verificare se una città non è presente nella lista
if 'New York' not in cities:
    print('New York non è presente nella lista.')
else:
    print('New York è presente nella lista.')



#6-1. Person: Use a dictionary to store information about a person you know. 
#Store their first name, last name, age, and the city in which they live. 
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

print(f"First name: {person['first_name']}")
print(f"Last name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")



#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. 
#Think of a favorite number for each person, and store each as a value in your dictionary. 
#Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.
favorite_numbers = {
    "Alice": 7,
    "Bob": 3,
    "Charlie": 11,
    "David": 17,
    "Eve": 23
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")


#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
glossary = {
    "variable": "A named storage location in a program",
    "function": "A block of code that performs a specific task",
    "loop": "A sequence of instructions that is repeated until a certain condition is met",
    "list": "An ordered collection of items that can be accessed individually",
    "dictionary": "A collection of key-value pairs that can be accessed using the keys"
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")



#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
#Loop through your list of people. As you loop through the list, print everything you know about each person.
people = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "city": "New York"
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 25,
        "city": "Chicago"
    },
    {
        "first_name": "Mike",
        "last_name": "Johnson",
        "age": 35,
        "city": "Los Angeles"
    }
]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()



#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. Next, loop through your list and as
#you do, print everything you know about each pet. 
pets = [
    {
        "kind": "dog",
        "owner": "John Doe"
    },
    {
        "kind": "cat",
        "owner": "Jane Smith"
    },
    {
        "kind": "bird",
        "owner": "Mike Johnson"
    }
]

for pet in pets:
    print(f"Kind: {pet['kind']}")
    print(f"Owner: {pet['owner']}")
    print()



#6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
#To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.
favorite_places = {
    "Ruth": ["Paris", "Tokyo", "New York"],
    "James": ["London", "Berlin", "Rome"],
    "Sam": ["Barcelona", "Amsterdam", "Sydney"]
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"- {place.title()}")


#6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
#Then print each person’s name along with their favorite numbers.
favorite_numbers = {
    "Alice": [7, 9, 13],
    "Bob": [3, 5],
    "Charlie": [11, 21, 27],
    "David": [17],
    "Eve": [23, 33, 43]
}
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")


#6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
#The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
cities = {
    "New York": {
        "country": "USA",
        "population": 8.4e6,
        "fact": "New York is known for its iconic skyline and cultural landmarks like the Statue of Liberty and Central Park."
    },
    "London": {
        "country": "UK",
        "population": 8.9e6,
        "fact": "London is the capital city of the UK and is known for its rich history, iconic landmarks, and cultural diversity."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 9.3e6,
        "fact": "Tokyo is the capital city of Japan and is known for its bustling streets, vibrant nightlife, and cutting-edge technology."
    }
}
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']:.2f} million")
    print(f"Fact: {info['fact']}")


#6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
#Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.
cities = {
    "New York": {
        "country": "USA",
        "population": 8.4e6,
        "fact": "New York is known for its iconic skyline and cultural landmarks like the Statue of Liberty and Central Park."
    },
    "London": {
        "country": "UK",
        "population": 8.9e6,
        "fact": "London is the capital city of the UK and is known for its rich history, iconic landmarks, and cultural diversity."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 9.3e6,
        "fact": "Tokyo is the capital city of Japan and is known for its bustling streets, vibrant nightlife, and cutting-edge technology."
    },
    "Paris": {
        "country": "France",
        "population": 2.2e6,
        "fact": "Paris is the capital city of France and is known for its iconic landmarks like the Eiffel Tower and the Louvre Museum."
    },
    "Rome": {
        "country": "Italy",
        "population": 2.9e6,
        "fact": "Rome is the capital city of Italy and is known for its rich history, ancient landmarks, and delicious cuisine."
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    country = info["country"].title()
    population = info["population"]
    fact = info["fact"]

    print(f"Country: {country}")
    print(f"Population: {population:.2f} million")
    print(f"Fact:\n{fact}\n")