
# * Python Basics

# * Python files are saved with the .py file extension
# * Python interpreter will 'read' them from top-to-bottom - so order is important

# * Comments
# * - hash marks at the beginning of the line denote a comment
# * - also used in dev (and sometimes prod) to 'comment out' code that isn't needed/working
# * - most editors have a comment toggle shortcut, that's very useful e.g. vs code 'ctrl + /'

# * Expressions

# * Expressions consist of values and operators which evaluate down to single value
print(2 + 2)
# ! 'print' function will display the evaluation of 2 + 2 but does not store it in a variable (more on that shortly)

# * Plenty of operators e.g. mathematical operators
# print(2 + 2) # addition
# print(4 - 2) # subtraction
# print(4 / 2) # division
# print(2 * 2) # multiplication

# * Slightly more advanced maths operators
# print(2 ** 3) # exponent (to the power of)
# print(22 // 8) # integer division (square root)
# print(22 % 8) # modulus (remainder)

# ? e.g. a practical use of the modulus operator is to determine whether a number os odd or even
# number_to_check = input('Enter a number ')
# if int(number_to_check) % 2 == 0:
#     print(f'{number_to_check} is even')
# else:
#     print(f'{number_to_check} is odd')

# * Order of operations for maths operators is important 
# ? PEMDAS i.e. parenthesis, exponents, multiplication, division, addition, subtraction
# print(2 + 3 * 6) # 20
# print((2 + 3) * 6) # 30

# * Data Types: integer, floating-point and strings

# * Data types are categories for values, each value has exactly one data type
# * - integers are whole numbers denoted by int()
# * - floating-points are numbers with decimal places, denoted by float()
# * - strings are text values, and can be wrapped in ' ' or " " and are denoted by str()

# ? You can check for types in python by using type()
# print(type(42))
# print(type(42.00))
# print(type('42'))

# ? If they're compatible, you can also cast values as different data types
# print(int(42.9)) # note that floats will round down
# print(str(42.9))
# print(int('42'))
# print(int('Forty')) # * example of incompatible value to cast, will throw an error

# * String Concatenation and Replication

# * One reason data types are important is because they can affect how an operator will work
# print('2' + '2') 
# print(2 + 2)

# * If you mix string and number data types with the + operator you will get an error
# print('2' + 2)
# print(2.5 + 2) # * because they're both number data types Python will evaluate this more flexibly

# * However, the * operator does allow you to mix string and int data types
# print('Library' * 5)
# print('Library' * 5.0) # * floats cannot be mixed with strings for multipliers

# * Storing values in variables

# * A variable is like a box where a value can be stored, which allows you to (re)use the value in elsewhere in the code
# name = 'Leo'
# print(name)
# other_name = 'Kos'
# print(other_name)
# print(name + other_name)
# name = name + other_name # * variables can also be updated or overwritten
# print(name)

# * Variable naming should be descriptive and specific
# ! variables names cannot contain spaces, use only words, letters and the underscore (_) character, it cannot begin with a number
# * Variable names are also case sensitive
# name = 'Leo'
# Name = 'Kos'
# print('name', name)
# print('Name', Name)
# ? it is convention in Python to use "snake_case" for naming variables i.e. all lower case separated by underscores

# * Your first program

print('What is your name?')
my_name = input()
print('It is good to meet you, ', my_name)
# print(f'It is good to meet you, {my_name}') #? a more modern way of combining variables and strings
print('The length of your name is: ')
print(len(my_name)) # len returns the length of a given variable/value
my_age = input('What is your age? ') # ? You can add a string to the input() function rather than create a sep print statement
print(f'You will be {int(my_age) + 1} in a year')
# ! note that the default type for an input is a str, so it needs to be converted to an int to allow for maths