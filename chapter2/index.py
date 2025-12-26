print('Yankees rule!')
print('But not in Boston!')

# The print function takes a variable number of arguments separated by commas

print('Yankees rule,','but not in Boston!')

# Scalar objects
# 1. int (-/+ nums)
# 2. float (decimal point nums)
# 3. bool (true/false)
# 4. None

# Objects and Operators
# - Combined to form Expressions

print(3 + 2)
print(3.0 + 2.0)
print(3 != 2)

# Finding object type

print(type(3))
print(type(3.0))
print(type('3'))

# <class 'int'>
# <class 'float'>
# <class 'str'>

# The primitive operators on type bool are and, or, and not

# Binding to variables

pi = 3
radius = 11
area = pi * (radius**2)
radius = 14

print(pi, radius, area, radius)
# 3, 14, 363, 14

# In Python, a variable is just a name, nothing more. Remember this—it is im-
# portant. An assignment statement associates the name to the left of the = symbol
# with the object denoted by the expression to the right of the =
# . Remember this
# too. An object can have one, more than one, or no name associated with it.

# The reserved words
# in Python 3 are and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, nonlocal, None, not, or,
# pass, raise, return, True, try, while, with, and yield.

# Python allows multiple assignment. The statement
# x, y = 2, 3
# binds x to 2 and y to 3

# Picking a random number

import random

randNum  = random.randint(1,128)
print(randNum)

# Declarative (Abstract), e.g square root of a number y * y = x
# Imperative (How-to, step by step)

# Types of computers
# - fixed program computers (e.g calculator)
# - stored program computers (the machine stores and executes the instructions, different tasks on the same machine)

# The computer only does what you tell it to do

# Where things can go wrong:
## 1. syntactic errors
## - common and easily caught
## 2. static semantic errors
## - some langs check for these before execution
## - can cause unpredictable behaviour
## 3. no sematic errors but different meaning than what the programmer intended
## - program crashes, stops running
## - program runs forever
## - program gives an answer but different than expected

# In Python programs manipulate 'data objects'
# Objects have a 'type' that defines the kinds of things programs can do to them
# Objects are 
# - scalar (cannot be subdivided, e.g the num 5)
# - non-scalar (have internal structure that can be accessed, e.g a list/seq of nums)

# Type casting
# - can convert an object of one type to another
# - e.g float(3) coverts to float 3.0
# - int(3.9) truncates float 3.9 to int 3

i, j = 22, 7
print(i+j)
print(i-j)
print(i*j)
print(i/j)
print(i%j)
print(i**j)

