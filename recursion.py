from colors import red
from django.utils.termcolors import colorize

# Sample recursion

def func_r(a):
    if a < 0:
        return 'Sorry, please enter a positive int like 5'
    print("Start: " + str(a))
    res = 0
    if a == 0:
        res = 0
    else:
        return func_r(a - 1) + 1
    print("End: " + str(a))
    return res


print("'Hello World' is overrated, say something")

# Fibonnaci sequence

print('Fibbonaci Sequence: ')
x, y = 0, 1
for i in range(10):
    print(x)
    x, y = y, x + y

# This is not related to recursion...

x = int(input('Enter a number to tell whether it\'s even or odd: '))
if x < 0:
   print('Please enter a number greater than 0')
elif x % 2 == 0:
   print('It is an even number')
elif x & 2 != 0:
   print('This is an odd number')
else:
   print(x)

# Factorials

factorial = 1
num = int(input('Enter a number to compute its factorial: '))

for i in range(1, num + 1): 
    factorial = factorial*i
print(factorial)

if num < 0:
   print(red('--------------------------------------------------'))
   print(red('FactorialError:            Traceback (most recent call last)'))
   print(red('---> Negative integer given '))
   print(colorize('SEARCH STACK OVERFLOW', fg='blue', opts=('bold', 'underscore')))
