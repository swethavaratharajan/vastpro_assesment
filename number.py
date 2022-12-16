#Write a program to find the sum of the series where x and n are passed from
# command line. The value of x must be passed as a command line argument when the
# program is invoked. (testing the usage of String[] args. If no argument is passed, then
# the program must provide an error message and exit gracefully.)
# 1+(x^1)/1!+(x^2)/2!+(x^3)/3!+...+(x^n)n! 




def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def sum(x, n):
    total = 1.0

    for i in range(1, n + 1, 1):
        total = total + (pow(x, i) / fact(i + 1))

    return total


if __name__ == '__main__':
    x = 5
    n = 4
    print("Sum is: {0:.4f}".format(sum(x, n)))

