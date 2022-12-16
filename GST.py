#Assume a flat GST of 18%. Write a program that accepts a product name and its
# selling price on the command line as a prompt from user. Calculate the GST and print
# the total bill amount with tax.






def Calculate_GST(org_cost, N_price):
    # return value after calculate GST%

    return (((N_price - org_cost) * 100) / org_cost);


# Driver program to test above functions

org_cost = 100

N_price = 120

print("GST = ", end='')

print(round(Calculate_GST(org_cost, N_price)), end='')

print("%")