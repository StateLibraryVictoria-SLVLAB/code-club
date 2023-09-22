
#* Flow Control

# * flow control important for determining which instructions get executed and in what order
# * flowcharts are a useful way to think about logic - and can be a really useful way of planning out your code

# * Boolean values
# * Two options `True` and `False` - note the capitalisation
True
False

spam = True
print(spam)

# spam = false # ! throws an error

# ? This is probably covered later in the book, but most programming languages have a concept of 'truthy' and 'falsy'
# ? A string is truthy, whereas an empty string is falsy e.g.
print('Truthy: ',bool('spam'))
print('Falsy: ',bool(''))
print('Truthy: ',bool(10)) # ints are truthy
print('Falsy: ',bool(0)) # except for zero
print('Truthy: ',bool(['a list'])) # a list with entries is truthy
print('Falsy: ',bool([])) # an empty list is falsy

# ? This can be really useful to use as part of flow control

# * Comparison operators
# * Compare two values and evaluate down to a single bool value:

my_score = 10

print(f'{my_score} equal to 10? ',my_score == 10)
print(f'{my_score} not equal 10? ',my_score != 10)
print(f'{my_score} less than 20? ',my_score < 20)
print(f'{my_score} greater than 5? ',my_score > 5)
print(f'{my_score} less than or equal to 10',my_score <= 10)
print(f'{my_score} greater than or equal to 15',my_score >= 15)

# * Mixing data types when comparing:
print(f'{my_score} equal to "10"? ',my_score == "10") #! An int cannot be equal to a string
print(f'{my_score} equal to 10.00? ',my_score == 10.00) #! Float and ints can be compared more directly

# * Boolean operators
# three operators `and`, `or` and `not` are used to compare bool values
# `and` and `or` always take two bool values

# * `and`
print(True and True) # both are True, so will return True
print(True and False) # both are not True, so will return False

# * `or`
print(True or True) 
print(True or False)
print(False or False)

# * `not` only operates on one bool value
print(not True)
print(not not True)

# * Mixing Boolean and comparison operators
# * Comparison operators evaluate to bool values, therefore they mix with Boolean operators

print((4 < 5) and (5 < 6))
print((4 < 5) and (9 < 6))
print((1 == 2) or (2 == 2))

# * Elements of flow control

# * Conditions: name given to a Boolean expression in the context of a flow control
# * Blocks of code: Python uses indentation to define 'blocks' of code e.g.

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted')
    else:
        print('Wrong password')
# ? Vs Code (and most IDEs) give you the option for collapsing blocks

# * blocks of code can be nested, and flow control helps to determine which are executed.

# * Flow control statements

# * `if` statement - if a condition is met, execute the code block nested within it
# * `else` statement - can only be used after an if statement, and will run when the condition is not met
# * `elif` ("else if") statement - can only follow an if statement, and contains another condition

name = 'Leo'
age = 1

if name == 'Kos':
    print('Hi Kos!')
elif name == 'Leo' and age > 1:
    print("You are not Leo, you're too old!")
elif age > 90:
    print("You're not Leo, Yiayia!")
elif name == 'Leo' and age == 1:
    print('Hello Leo!')

# ! The order of elif statements is important, so plan out the logic of your program with care!

# * While  loop

# * `while` statements can be made to execute code over and over again (potentially infinitely)
# * Code in a `while` block will be executed whilst the statement condition is `True`
# * Syntax is similar to an `if` statement

spam = 0
if spam < 5:
    print('Hello, world')
    spam += 1 # ? '+=' can be used to increment by  a value
print('Spam value after if: ',spam)

spam = 0
while spam < 5:
    print('Hello world')
    spam += 1
print('Spam after while ', spam)

# ! It can be quite easy to define a while loop that never closes e.g.

# spam = 10
# while spam >= 10:
#     print(f"SPAM, SPAM, SPAM! {spam}")
#     spam += 1

# * Break statements
# * `break` keyword can be used to exit a loop, whether or not the condition has been met e.g.

# while True:
#     print('Please type your name')
#     name = input()
#     if name == 'Kos':
#         break
# print(f'Thank you {name}!')

# * Continue statement
# * `continue` used inside loops, move back the execution to the beginning of the loop

# while True:
#     name = input('Who are you? ')
#     if name != 'Leo':
#         continue
#     print('Hello, Leo. How old are you? ')
#     age = input()
#     if age == 1:
#     # if age == '1':
#         break
# print('Hello Leo!')

# * For loops and the `range()` function

# * `for` loops will run a finite number of times (as opposed to while which is potentially infinite)
# ? in reality in most (all?) cases you can design code to achieve the same function using either `for` or `while` but it's good to make an active and informed choice!
# * the `range()` function returns a sequence of numbers, https://www.w3schools.com/python/ref_func_range.asp

print('My name is')
for i in range(5):
    print(f'Leo five times {i}')
# ? `i` is used as a temporary variable and refers to each number in the sequence defined in `range(5)`
print('My name is')
i = 0
while i < 5:
    print(f'Kos five times {i}')
    i += 1

# * `range() has three optional arguments:
# * 'start' the number at which the range will start
# * 'stop' the number it'll stop at
# * 'step' the amount the range will increment by for each iteration
for i in range(12,26, 2):
    print(i)

# * Importing modules

# * Python comes with the inbuilt 'standard library' that gives access to a range of modules
# * Modules can be imported to a script and the functions contained within can be used
# * `import` key word is used to import. It is common/best practice to import modules at the top of the script

import random
for i in range(5):
    print(random.randint(1,10))

# ? You can also import specific functions from a module
# from random import randint
# for i in range(5):
#     print(randint(1,10))