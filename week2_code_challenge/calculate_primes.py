__author__ = 'root'
import math

print('Generate a list of prime numbers to x: ')
max_number = raw_input('x >')
max_number = int(max_number)
for num in range(1, max_number):  # 11 iterations
    if all((num % i == 0) for i in range(2, int(math.sqrt(num))+1)):
        print(num)

