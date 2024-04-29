# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizze = ['capricciosa', 'margherita', 'diavola']

for pizza in pizze:
    print(f"Mi piace la pizza {pizza}.")


print("Mi piace molto la pizza!")

print()
print()

#4-2. Animals: Think of at least three different animals that have a common characteristic. 
#Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
#• Modify your program to print a statement about each animal, such as A dog would make a great pet.
#• Add a line at the end of your program, stating what these animals have in common. 
#You could print a sentence, such as Any of these animals would make a great pet!

animali_simili = ['pinguino', 'foca', 'leone marino']


for animale in animali_simili:
    print(f"Un {animale} è un mammifero marino.")


print("Questi animali hanno tutti in comune il fatto di essere mammiferi marini!")

print()
print()

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for i in range(1, 21):
    print(i)

print()
print()



#4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
#(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

#for number in range(1, 1000001):
#    print(number)

print()
print()

#4-5. Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and ends at one million. 
#Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))

min_num = min(numbers)
max_num = max(numbers)
print(f"Il numero minimo è {min_num} e il numero massimo è {max_num}.")

total = sum(numbers)
print(f"La somma dei numeri da 1 a 1 milione è {total}.")

print()
print()

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

numeri_dispari = list(range(1, 21, 2))


for numero in numeri_dispari:
    print(numero)

print()
print()

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multipli_di_tre = [3 * i for i in range(1, 11)]
for multiplo in multipli_di_tre:
    print(multiplo)

print()
print()

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubi = [i**3 for i in range(1, 11)]
for c in cubi:
    print("Il cubo di", cubi.index(c)+1, "è:", c)

print()
print()


#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.
cubes = [i**3 for i in range(1, 11)]

print("The first three items in the list are:", cubes[:3])
print("Three items from the middle of the list are:", cubes[4:7])
print("The last three items in the list are:", cubes[-3:])

print()
print()

