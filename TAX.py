#Modify the above tax program to accept an ‘n’ number of product names, their prices
# in a loop. The program should continue to prompt the user, “enter next product”, till
# the user types “e” for end. The program should then add all the product prices
# entered, calculate the sales tax and print the total bill amount with the proper splitup
# prices also printed.




productName = []
productAmount = []
# amount=0
keep_going = True
while keep_going:
    name = input('Enter your name, or type e to end :  ')
    if name == "e":
        keep_going = False
    else:
        pAmount = int(input("Enter product amount :  "))

    if name != "e":
        productName.append(name)
        productAmount.append(pAmount)

    if name == 'e':
        amount = sum(productAmount)
        tax = (amount * (18 / 100))
        print("product Total Amount :", amount, '\n',
              "Sales Tax :", tax, '\n',
              "final Amount :", amount + tax, '\n')