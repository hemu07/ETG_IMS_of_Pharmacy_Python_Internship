#Inventory Management System of a PHARMACY
#Open database file
import random
import datetime
import json
a = open('file1.json', 'r')
b = a.read()
database = json.loads(b)          # create dict from string
a.close()

print("Welcome to Inventory Management System of Cosmetics Pharmacy \n")
print('Menu : ')
print("A : Add product")
print("R : Remove product")
print("E : Customize your product")
print("L : show list of all products")
print("I : Inquire about a product")
print("P : Purchase a product")
print("C : Checkout your cart ")
print("S : Show all products purchased")
print("Q : Quit")
print("remove : Remove an product from the cart")
print("help : See all commands again")
print('\n')
cart = []
command = "yes"
pro_name = {}
total_quantity = 0
total_cost = 0
flag = 0
user = input('Enter Your Name: ')
print('Welcome {} to our Pharmacy...'.format(user))
while command.upper() != "Q":
    command = input("enter your order... ")
    if command.upper() == "Q":
        break
    elif command.upper() == "A":
        product_id = (input("Enter product number: "))
        if product_id in database.keys():
            print("Product ID already exist")
            print("Are you sure, you wanna edit the Product?")
            d = input("If yes enter 'y' else 'n':")
            if d.upper() == 'Y':
                print('\n')
            elif d.upper() == 'N':
                product_id = input("Enter product number: ")
                if product_id in database.keys():
                    print("This Product ID also already exist")
                    print("Enter you choices again")
                    continue
            else:
                print("Please enter in valid character")
                continue
        category_ui = input("Enter product category: ")
        name_ui = input("Enter product name: ")
        price_ui = float(input("Enter product price: "))
        details_ui = input("Enter product description: ")
        quantity_ui = int(input("Enter product Quantity: "))

        if quantity_ui < 0:
            print("quantity cannot be less than zero, Enter 'a' again ")
            continue

        database[product_id] = {'Category': category_ui, 'Product_name': name_ui, 'Details': details_ui, 'Quantity': quantity_ui, "Price ": price_ui}
        print('{', 'Product ID: ', product_id, ", ", "Category: ", category_ui, ", ", "Product Name: ", name_ui, ", ","Details: ", details_ui, ", ", "Quantity: ", quantity_ui, ", ", "Price: ", price_ui, "}")
        print('Item was successfully added.')

    elif command.upper() == "E":
        product_id = input("Enter product ID: ")
        if product_id in database.keys():
            name_ui = input('Enter the product name: ')
            price_ui = float(input("Enter product price: "))
            details_ui = input("Enter product details: ")
            quantity_ui = int(input("Enter product quantity: "))

            if quantity_ui < 0:
                print('quantity cannot be negative')
                q = input("Enter 'c' to rewrite the quantity, else quantity will be set to 0")
                if q.upper() == 'C':
                    quantity_ui = int(input("Enter product quantity: "))
                    if quantity_ui < 0:
                        print("Quantity cannot be Negative, Setting the Quantity to 0")
                        quantity_ui = 0
                        print('Quantity: ', quantity_ui)
                else:
                    quantity_ui = 0
                    print('Quantity of Product is now set to 0.')
                    print('Quantity: ', quantity_ui)

            database[product_id] = {'Category':category_ui, 'Product_name': name_ui, 'Details': details_ui, 'Quantity': quantity_ui, "Price ": price_ui}
        else:
            print("item does not exist, to add an item use 'a'")

    elif command.upper() == "R":
        product_id = input("Enter Product ID: ")

        if product_id in database.keys():
            check = input("Do you want to remove that item? enter 'y' or 'n' ")
            if check.upper() == "Y":
                p = database.pop(product_id)
                print('Product', p, 'deleted successfully')
        else:
            print("Sorry, no such product exists")
    elif command.upper() == "L" :
        unique = set()
        for i in database.keys():
            unique.add(database[i]['Category'])
        category = list(unique)
        print('All the valid Product IDs:\n ', list(database.keys()))
        print("All product categories:\n ", list(unique))
        print("Product Menu--\n ")
        for j in range(len(category)):
            print('\t', '---------------------------------------')
            print('\t', '      | ', category[j], ' |')
            print('\t', '---------------------------------------')
            for i in database.keys():
                if database[i]['Category'] == category[j]:
                    print('Prod ID: ', i, ',  ', 'Product Name: ', database[i]['Prod_name'], ',  ', 'Price: Rs.',
                          database[i]['Price Rs.'], ',  ', 'Quantity: ', database[i]['Quantity'])

    elif command.upper() == "I" :
        product_id = input("Enter Product IDs: ")
        if product_id in database.keys():
            print("Product ID: ", product_id, ', ', 'Product Name: ', database[product_id]['Prod_name'], ',', " Description: ",
                  database[product_id]['Description'], ', ', " Price: ", database[product_id]['Price Rs.'], ', ', " Quantity: ",
                  database[product_id]['Quantity'])
            if (database[product_id]['Quantity'] < 3 and database[product_id]['Quantity'] != 0):
                print("*****Only ", database[product_id]['Quantity'], " remaining! Hurry!*****")
        else:
            print("Sorry, no such product exists!")

    elif command.upper() == "P" :
        product_id = input("Enter the product_Id: ")
        if product_id in database.keys():
            order_quantity = int(input("Enter the quantity: "))
            if order_quantity < 0:
                print('You cannot order 0 quantity!!')
                order = input("Enter 'y' to continue ordering:")
                if order.upper() == 'Y':
                    order_quantity = int(input("Enter the quantity: "))
                    if order_quantity < 0:
                        print('You cannot order 0 quantity!!')
                        print("Enter 'p' to place the order  again. ")
                        continue
                    else:
                        print('\n')
                else:
                    print("Enter 'p' to place the order  again. ")
                    continue
            if flag == 1:
                flag = 0
            stock = database[product_id]['Quantity']
            if stock == 0:
                print("Sorry !! We don't have product in stock.")
            elif stock < order_quantity:
                print("Sorry!! We only have ", stock, 'stocks left!!')
                print('You can order', stock, 'Stock or you can select anything else from the list.')
                print("To see the List enter 'L'.")
            else:
                item_price = database[product_id]['Price Rs.'] * order_quantity
                print("Product Name: ", database[product_id]['Prod_name'])
                print("Price : ", database[product_id]['Price Rs.'])
                total_cost = total_cost + item_price
                database[product_id]['Quantity'] = database[product_id]['Quantity'] - order_quantity
                print('Product ', database[product_id]['Prod_name'], ' with ', order_quantity, 'quantity ', 'added to cart:', 'Rs.', item_price)
                cart.append(product_id)
                pro_name[database[product_id]['Prod_name']] = {'Qty': order_quantity, 'MRP': database[product_id]['Price Rs.'], 'GST': 18, 'Amount': item_price}
                print("Enter 'P' to purchase again!!")
        else:
            print('Product ID does not exist!!')
            print("Please enter valid Product ID, enter 'l' to know about all")

    elif command.upper() == "C":
        print("You bought the following products: ", cart)
        d = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day)
        date = str(d)
        t = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
        time = str(t)
        for k in pro_name.keys():
            print('Product Bought:', k, ', ', 'Quantity Bought:', pro_name[k]['Qty'])
        print("\n")
        print('\t', '---------------------------------------')
        print('\t', '\t', 'COSMETICS PHARMACY ')
        print('\t', '---------------------------------------')
        print('\t', "Order No. Take Out", '\t', 'Tax Invoice')
        print('------------------------------------------------------------------------------------------')
        print('Bill No.: ', round((random.uniform(1, 10)) * 1000), '\t', 'Bill: ', 'Cash Bill')
        print('Counter: ', 'CASH1', '\t', 'Date: ', date)
        print('User: ', user, '\t', '  ', 'Time: ', time)
        print('------------------------------------------------------------------------------------------')
        print('Product Name', '        |   ', '\t', '   ', 'Qty', '   |   ', 'MRP', '   |   ', 'GST%', '  |  ','Amount', '  |')
        print('------------------------------------------------------------------------------------------')
        for v in pro_name.keys():
            print()
            print(v, '    |    ', pro_name[v]['Qty'], '    |   ', pro_name[v]['MRP'], '    |    ', pro_name[v]['GST'], '    |    ', pro_name[v]['Amount'])
            total_quantity += pro_name[k]['Qty']
        print("\n")
        print('------------------------------------------------------------------------------------------')
        print('Total Qty: ', total_quantity, '              ', "Gross: ", "Rs.", round(total_cost, 2))
        tax = round(0.18 * total_cost, 2)
        print('Total Products: ', len(pro_name.keys()), '               ', "Tax is 18%: ", "Rs.", tax)
        total = round(total_cost + tax, 2)
        print("\n")
        print('------------------------------------------------------------------------------------------')
        print("Total including Tax: ", '   ', "Rs.", total)
        print('------------------------------------------------------------------------------------------')
        total_cost = 0
        flag = 1
        print("\n")
        print("You can still purchase items after check out, your cart has been reset. To quit press q")
        print("\n")

    elif command.upper() == "HELP":
        print("A-Add an Product")
        print("R-Remove an Product")
        print("E-Edit specifics of an Products")
        print("L-List all the Products")
        print("I-Inquire about a product ")
        print("P-Purchase a product")
        print("C-Checkout")
        print("S-Show all products purchased")
        print("Q-Quit")
        print("remove-Remove an product from the cart")
        print("help-See all commands again")

    elif command.upper() == "Remove":
        print('It will remove only 1 product quantity at a time')
        print("You can quit by 'q' and reset the cart also by entering 'n'.")
        check = input("Are you sure you want to remove an Product from the cart(y/n)? ")

        if check.upper() == "Y":
            product_id = input("Enter the product_Id: ")

            if product_id in cart:
                item_price = database[product_id]['Price Rs.'] * 1
                print("Product Name: ", database[product_id]['Prod_name'])
                print("Price : ", database[product_id]['Price Rs.'])
                total_cost = total_cost - item_price
                database[product_id]['Quantity'] = database[product_id]['Quantity'] + 1
                j = 0
                for i in range(0, len(cart)):
                    if i == product_id:
                        j = i
                cart.pop(j)
                print('Product ', database[product_id]['Prod_name'], ' with ', '1', 'quantity ',
                      'removed from cart having price :', 'Rs.', item_price)
                print("\n")
            else:
                print("\n")
                print("That item is not in your cart!")

    elif command.upper() == "S":
        print(cart)
        print('-------------------------------------------------------------------------------------')
        for k in pro_name.keys():
            print('Product Bought:', k, ', ', 'Quantity Bought:', pro_name[k]['Qty'])
        print('-------------------------------------------------------------------------------------')
    else:
        print("ERROR! Please make choices correctly!")
        print("Enter 'help' to know all the existing commands.")

if total_cost > 0 and flag == 0:
    d = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
        datetime.datetime.now().day)
    date = str(d)
    t = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(
        datetime.datetime.now().second)
    time = str(t)
    print('\t', '-------------------------------------------')
    print('\t', '\t', 'Inventory Management System')
    print('\t', '-------------------------------------------')
    print("Order No. Take Out", '\t', '\t', 'Tax Invoice')
    print('------------------------------------------------------------------------------------')
    print('Bill No.: ', round((random.uniform(1, 10)) * 1000), '\t', 'Bill: ', 'Cash Bill')
    print('Counter: ', 'CASH1', '\t', 'Date: ', date)
    print('User: ', user, '\t', '  ', 'Time: ', time)
    print('------------------------------------------------------------------------------------')
    print('Product Name', '\t', '            | ', '  ', 'Qty', '   ', '  |  ', 'MRP', '   ', '  |  ', 'GST%', '   ',
          '  |  ', 'Amount', '  |  ')
    print('------------------------------------------------------------------------------------')
    for v in pro_name.keys():
        print("\n")
        print(v, '     ', '   |   ', pro_name[v]['Qty'], '   |   ', pro_name[v]['MRP'], '   |   ', pro_name[v]['GST'], '   |   ',
              pro_name[v]['Amount'], '   |  ')
        total_quantity += pro_name[v]['Qty']
    print("\n")
    print('----------------------------------------------------------------------------')
    print('Total Qty: ', total_quantity, '         ', "Gross: ", "Rs.", round(total_cost, 2))
    tax = round(0.18 * total_cost, 2)
    print('Total Products: ', len(pro_name.keys()), '        ', "Tax is 18%: ", "Rs.", tax)
    total = round(total_cost + tax, 2)
    print("\n")
    print('----------------------------------------------------------------------------')
    print("Total including Tax: ", '   ', "Rs.", total)
    print('----------------------------------------------------------------------------')
print("\n")
print('\t', "Thank you for using IMS, See you again!")
jsonfile = json.dumps(database)
a = open("records1.json", 'w')
a.write(jsonfile)
a.close()