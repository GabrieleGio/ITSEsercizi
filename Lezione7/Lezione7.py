#1. Write a new class called Food, it should have name, price and
#description as attributes.
#2. Instantiate at least three different foods you know and like.
#3. Create a new class called Menu, it should have a list (of Foods) as attribute.
#__init__ should take a list of Foods as optional parameters (default=[])
#4. Create a addFood() and removeFood() for the Menu
#5. Create a few new Food instances. Add each to the Menu using the respective
#Method.
#6. Add a method printPrices() that list all items on the Menu with their
#prices.
#7. Add a Menu method getAveragePrice() that returns the average Food
#price of the Menu

class Food:
    def __init__(self,name,price,description):
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self):
        self.lista_cibi = []

    def addFood(self,food):
        self.lista_cibi.append(food)

    def removeFood(self,food):
        self.lista_cibi.pop(food)

    def printPrices(self):
        for food in self.lista_cibi:
            print(f"Il costo di {food.name} è {food.price} euro")
    
    def getAveragePrice(self):
        somma = 0
        for food in self.lista_cibi:
            somma += food.price
        media = somma / len(self.lista_cibi)
        print(f"La media dei prezzi del menù è {media} euro")
    
    
menu = Menu()
pizza = Food("Pizza",8,"very good for dinner")
pasta = Food("Pasta",12,"very good for launch")
milk = Food("Milk",4,"very good for breakfast")

menu.addFood(pizza)
menu.addFood(pasta)
menu.printPrices()
menu.getAveragePrice()
