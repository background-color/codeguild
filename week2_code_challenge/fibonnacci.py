__author__ = 'root'


def fib(n):
    # declare variables a and b
    a, b = 1, 1
    # iterate numbers through the user input (n)
    for i in range(n):
        # swaps b into variable a and a+b into variable b allowing us
        a, b = b, a + b
        print a

print('This program calculates the Fibonnacci number to the number you input:')
user_input = raw_input('>')
x = int(user_input)

print fib(x)
