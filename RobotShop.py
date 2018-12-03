

class Product:
    def __int__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


products = [Product("Ultrasonic Range Finder", 2.50, 4),
            Product("Servo Motor", 14.99, 10),
            Product("Servo Controller", 44.95, 5),
            Product("Microcontroller", 34.95, 7),
            Product("Laser Range Finder", 149.99, 2),
            Product("Lithium Polymer Battery", 8.99, 8)]
            


def printStock():
    print()
    
    print("Available Products")
    
    print("------------------")
    
    for i in range(0,len(products.name)):
        if products.stock[i] > 0:
            print(str(i)+")",products.name[i], "$", products.price[i])
            print()


 
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "quit": break
        
        prodId = int(vals[0])
        
        count = int(vals[1])
        
    if products.stock[prodId] >= count:
         if cash >= products.price[prodId] * count:
             products.stock[prodId] -= count
             cash -= products.price[prodId] * count
             print("You purchased", count, products.name[prodId]+".")
             print("You have $", "{0:2f}".format(cash), "remaining.")
         else:
             print("Sorry, you cannot afford that product.")

    else:
        print("Sorry, we are sold out of", products.name[prodId])

main()

