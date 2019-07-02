import math

print('Hello Python.')
print('My Learning code samples for Python Programming')

name = 'Sachin'
age = 42
is_new = False
greeting = input('What''s your name? ')
fav_color = input('What is your favorite color? ')
print(greeting + ' likes ' + fav_color)

weight_lbs = input('Enter your weight in pounds ')
weight_kgs = float(weight_lbs) * 0.4535
print(f'Your weight in Kilograms:{weight_kgs} kgs')

course = 'Bob is a software developer'
diff_var = course[:]
diff_var += ' with 15 years experience.'
print(diff_var)
print(course)

# Formatted Strings
first = 'Hello'
second = 'World!!!'
message = f'{first}, {second} is my first program for formatted strings'
print(message)

# String Methods
msg = 'Sample message to explain the String methods'
print(f'The length of msg string is {len(msg)}')
print(f'To Upper: {msg.upper()}')
print(f'To Lower: {msg.lower()}')
print(f'To Title: {msg.title()}')
print(msg)
print(msg.find('e'))
print(msg.find('M'))
print(msg.replace('message', 'Message'))
print('message' in msg)  # in operator returns boolean
print('Explain' in msg)  # in operator returns boolean

# Arithmetic Operations
print(9 // 4)  # returns the Quotient
print(9 % 4)  # returns the Remainder
print(5 ** 3)  # returns the Exponential value 5*5*5

# Math Functions
print(math.floor(3.5))
print(math.ceil(4.2))
print(math.factorial(5))

# If Statements
lp = 12
if lp > 10:
    print('Greater than 10')
    print('Greater than 10 again')
elif lp == 10:
    print('Value is 10')
else:
    print('Lesser than 10')

is_buyer_credit_good = False

if is_buyer_credit_good:
    print(f'Please pay 10% down payment which is:{1000000 * 0.1}')
else:
    print(f'Please pay 20% down payment which is:{1000000 * 0.2}')

# Logical Operators AND, OR , NOT

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('Eligible for loan')

has_good_credit = False

if has_high_income or has_good_credit:
    print('Still Eligible for Loan')

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print('No Criminal Record. So, Eligible for Loan')

# Comparison Operators
name = 'Arnold Schwarzeneggar'
if len(name) < 5:
    print('Name is too short')
elif len(name) > 30:
    print('Name is too long')
else:
    print('Name is valid')

# Weight Converter
weight = input('Weight:')
pounds_or_kgs = input('(L)bs or (K)gs:')
if pounds_or_kgs.upper() == "L":
    print(f' Your Weight: {float(weight) * 0.45} kgs')
elif pounds_or_kgs.upper() == "K":
    print(f' Your Weight:{float(weight) / 0.45} lbs')
else:
    print('Invalid Input')

# While Loop

counter = 1
while counter <= 10:
    print(f"The While Loop value is: {counter}")
    counter = counter + 1

# Star Loop

star_counter = 0

while star_counter <= 5:
    print('*' * star_counter)
    star_counter = star_counter + 1
else:
    while star_counter > 0:
        print('*' * star_counter)
        star_counter = star_counter - 1

# Print Letter F

numbers = [5, 2, 5, 2, 2]

for k in numbers:
    print('X' * k)

print()
print('------------------------------------')

for num in numbers:
    result = ''
    for i in range(num):
        result += 'X'
    print(result)

# Lists
st_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for sn in st_numbers:
    print('X' * sn)

print(st_numbers)
print(st_numbers[2:])
print(st_numbers[-3])
print(st_numbers[4:7])

largest_numbers = [3, 8, 6, 4, 10]
max_num = largest_numbers[0]

for mn in largest_numbers:
    if max_num < mn:
        max_num = mn
print(max_num)

# 2D Lists

matrix = [
            [2, 5, 8],
            [1, 4, 7],
            [3, 6, 9]
         ]

print(matrix[1][0])



