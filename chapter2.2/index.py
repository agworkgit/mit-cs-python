# Branching Programs

if 3 < 5:
    print('No')
else:
    print('Yes')

# prints 'No'

# Even or odd?
x = 15

if x % 2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditionals')

# prints 'Odd' and 'Done with conditionals'

# Nested Conditionals in Python

if x % 2 == 0:
    if x % 2 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x % 3 == 0:
    print('Divisible by 3 and not by 2')

# prints 'Divisible by 3 and not by 2'
# The elif in the above code stands for “else if.”

# Compoud Boolean Expressions

x, y, z = 5, 10, 15

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')

# prints 'x is least'

# Finger Exercise

if x or y or z % 2 != 0:
    print('odd')
    if x > y and x > z:
        print('x largest')
    if y > x and y > z:
        print('y largest')
    if z > x and z > y:
        print('z largest')
else:
    print('even')

# 'odd, z largest'

# Finding str length

print(len('blue'))
# 4

# Indexing
print('something'[-1])
# g

# Slicing substrings - str[start:end]
print('abc'[1:3])
# bc

# python3 <filename> to interpret input commands

# Getting input from the user
# The raw input will be returned as a string and must be type cast if number or boolean!

name = input('Enter your name: ')
print('Are you really', name, '?')

num = float(input('Enter an integer: '))
print(type(num))