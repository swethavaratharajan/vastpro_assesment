# floyd's triangle
#1  
#0  1  
#0  1  0  
#1  0  1  0  
#1  0  1  0  1  




rows = 5
number = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number%2, end = '  ')
        number = number + 1
    print()