#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if (number < 0):
    ld *= -1
print('Last digit of ', number, 'is ', end='')

if (ld > 5):
    print(ld, 'and is greater than 5')
elif (ld == 0):
    print(ld, 'and is zero')
else:
    print(ld, 'and is less than 6 and not 0')
