#========The beginning of the class==========

#create the new class called Shoe, and initialise the attributes

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #methods that returns the cost of the shoes.
    def get_cost(self):
        return self.cost

    #methods that returns the quantity of the shoes.
    def get_quantity(self):
        return self.quantity

       #methods that returns the string presentation of the class
    def __str__(self):
        return(f"""
    Country: {self.country}
    Code: {self.code}
    Product: {self.product}
    Cost: {self.cost}
    Quantity: {self.quantity}""")


#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============

#method that read the external file, and store the data in the list
def read_shoes_data():
    try:
        file = open("inventory.txt","r")
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            country, code, product, cost, quantity = line.split(",")
            shoe_list.append(Shoe(country, code, product, cost, quantity))
    except Exception as error:
        print("Error:")
        print(error)
    finally:
        file.close()

#method that ask user for the data, and create a class by the data
def capture_shoes():
    try:
        file = open("inventory.txt","a")
        new_country = input("Please enter the country of the new shoes: ")
        new_code = input("Please enter the code of the new shoes: ")
        new_product = input("Please enter the product of the new shoes: ")
        new_cost = input("Please enter the cost of the new shoes: ")
        new_quantity = input("Please enter the quantity of the new shoes: ")
        
        #write the new shoe data in the external file
        newshoe_data = f"{new_country},{new_code},{new_product},{new_cost},{new_quantity}"
        file.write(f"\n{newshoe_data}")
        print("Input new shoe successful.")
    
    except Exception as error:
        print("Error:")
        print(error)
    finally:
        file.close()

#method that print out the Shoe class data in the list
def view_all():
    read_shoes_data()
    
    for i in range(len(shoe_list)):
        print((shoe_list[i]))

#method that print out the lowest quantity shoe, and ask if the user wants to restock
def re_stock():
    read_shoes_data()
    lowest_quantity = None
    lowest_stock_shoe = None
    for i in range(len(shoe_list)):
        data = shoe_list[i]
        if lowest_quantity == None:
            lowest_quantity = int(data.quantity)
            lowest_stock_shoe = data.product
            index = i
        elif lowest_quantity > int(data.quantity):
            lowest_quantity = int(data.quantity)
            lowest_stock_shoe = data.product
            index = i

    #if user wants to restock, update the stock accordingly
    restock_option = input(print(f"{lowest_stock_shoe} has only {lowest_quantity} left, do you want to restock it?(Y/N) ")).lower()
    if restock_option == "y":
        restock_quantity = int(input(print("How many do you want to restock? ")))
        new_quantity = lowest_quantity + restock_quantity
        shoe_list[index].quantity = new_quantity
        print(f"{lowest_stock_shoe} new stock amount: {new_quantity}")
    
    else: 
        print(f"OK! Did not restock {lowest_stock_shoe}")

#method that allow user to search shoe by enter the product code
def seach_shoe():
    read_shoes_data()
    shoe_found = False
    code_input = input("Please input the shoe code: ")
    for i in range(len(shoe_list)):
        if shoe_list[i].code == code_input:
            print(shoe_list[i])
            shoe_found = True
            break
    if shoe_found == False:
        print("Shoe not found, please double check the code!")

#method that calculate the total value of the shoe
def value_per_item():
    read_shoes_data()
    for i in range(len(shoe_list)):
        shoevalue = int(shoe_list[i].cost) * int(shoe_list[i].quantity)
        product = shoe_list[i].product
        quantity = shoe_list[i].quantity
        print(f"""
    Product: {product} 
    Total pairs: {quantity}
    Total value: {shoevalue}
    """)

#method that set the highest quantity product on sale
def highest_qty():
    read_shoes_data()
    highest_quantity = None
    highest_stock_shoe = None
    for i in range(len(shoe_list)):
        if highest_quantity == None:
            highest_quantity = int(shoe_list[i].quantity)
            highest_stock_shoe = shoe_list[i].product
        if int(shoe_list[i].quantity) > highest_quantity:
            highest_quantity = int(shoe_list[i].quantity)
            highest_stock_shoe = shoe_list[i].product
            index = i
    print(f"{highest_stock_shoe} now is on sale.")

#==========Main Menu=============

#main menu and take the user input as instruction and perform different function
while True:
    
    option = input("""
    Welcome back, please select one of the following option below:
    VA - View all shoe 
    CS - Capture new shoe
    RS - Re-stock
    SS - Search shoe
    CV - Calculate the value
    HQ - Highest Qty
    -1 - exit
    
    """).lower()

    if option == "va":
        view_all()
    elif option == "cs":
        capture_shoes()
    elif option == "rs":
        re_stock()
    elif option == "ss":
        seach_shoe()
    elif option == "cv":
        value_per_item()
    elif option == "hq":
        highest_qty()
    elif option == "-1":
        print("Goodbye!")
        break
    else:
        print("Error! Invaild input! Please try again")