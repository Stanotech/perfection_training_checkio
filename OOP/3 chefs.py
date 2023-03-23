class AbstractCook:   
    def __init__(self):
        self.total_food = 0
        self.total_drink = 0

    def add_food(self, amount, cost):
        self.total_food += amount*cost
        
    def add_drink(self, amount, cost):
        self.total_drink += amount*cost
        
    def total(self):
        return (f"{self.food}: {self.total_food}, {self.drink}: {self.total_drink}, Total: {self.total_food + self.total_drink}")
        

class JapaneseCook(AbstractCook):    
    food, drink = "Sushi", "Tea"

class RussianCook(AbstractCook):
    food, drink = "Dumplings", "Compote"    

class ItalianCook(AbstractCook):
    food, drink = "Pizza", "Juice"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
