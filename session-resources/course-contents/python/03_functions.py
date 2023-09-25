
# * Functions

# * Already encountered some in-built functions e.g. `print()`, `input()` and `len()`
# * Python makes it easy to create your own functions, which are building blocks to most functional codebases
# * Functions are reusable 'mini-programs'

# def used to define a function
def hello():
    print('Howdy')
    print('Howdy!!')
    print('Hello there')

# without being 'called' a function will remain unused
hello()

# * Major purpose of functions is to group code that gets called multiple times

# * Parameters
# * Functions can be parameterised with 'arguments' e.g. `print('Hello')`

def hello(name):
    print(f'Hello {name}')

hello('Leo')

# * Return statement
# * `return` is a reserved word in Python - used to return (geddit) a value from a function
# * Functions can have 0 to many return statements

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# * None value

# * The only value of the `NoneType` data type