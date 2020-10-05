# Defining a List
aeroplanes = ['Airbus', 'Boeing', 'Concorde']
print(aeroplanes)

# Accessing a List
print(f'Getting the list item based on index: {aeroplanes[1]}')

# Accessing the last item in the list
print(aeroplanes[-1])

# Changing, Adding and Removing Items from the list

formula_1 = ['Ferrari', 'Mercedes', 'Aston Martin', 'Alfa Romeo', 'Renault', 'Williams']
print(formula_1)

print('Modifying the list item at index 3')
formula_1[3] = 'Haas Racing'
print(formula_1)

print('Adding a Racing Team to the Formula 1 list using append() method')
formula_1.append('Alfa Romeo')
print(formula_1)

print('Adding a Racing Team to the Formula 1 list using insert() method')
formula_1.insert(4, 'Torro Rosso')
print(formula_1)

print('Removing a Racing Team from the Formula 1 list using del statement')
del formula_1[5]
print(formula_1)

print('Popping a Racing Team from the Formula 1 list using pop() method')
popped_team = formula_1.pop()
print(formula_1)
print(popped_team)

print('Popping a Racing Team from the Formula 1 list using pop() method with an index')
popped_team = formula_1.pop(2)
print(formula_1)
print(popped_team)

print('Removing a Racing Team from the Formula 1 list using remove() method')
team = 'Ferrari'
formula_1.remove(team)
print(formula_1)
print(f'{team} has been removed')

numbers = [3, 5, 9, 1, 4, 2, 6, 8, 7]
print(numbers)
numbers.sort()
print(f'After Sorting: {numbers}')


alphabets = ['B', 'D', 'A', 'C']
print(alphabets)
print('Temporarily Sorting using Sorted function')
print(sorted(alphabets))
print(f'Again back to Original List: {alphabets}')

print('Printing the list in reverse order')
alphabets.reverse()
print(alphabets)


print('To find the length of the list')
print(f'The length of the list alphabets is: {len(alphabets)}')


# Working with the lists
# Looping through the list

riders = [4, 9, 12, 19, 20, 21, 26, 30, 35, 36, 41, 42, 46, 88, 93, 99]

for rider in riders:
    print(f'The rider number is: {rider}')

calendars = ['Qatar', 'Thailand', 'COTA', 'Aragon']
for cal in calendars:
    print(f'The race calendar circuit: {cal.title()}')

worldChampions = ['rossi','lorenzo','marc']
for wc in worldChampions:
    print(f'The World Champion is: {wc.title()}')
print('End of statements')

for i in range(1, 11):
    print(f'The Range value is: {i}')
print('End of range() function')

for i in range(1, 15, 2):
    print(f'The Range value is: {i}')
print('End of range() function')

nums = list(range(1, 5))
for i in nums:
    print(f'The Range value is: {i}')
print('End of range() function')

squares = []
for j in range(1, 11):
    squares.append(j ** 2)
print(squares)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'The Minimum value: {min(digits)}')
print(f'The Maximum value: {max(digits)}')
print(f'The Sum of values: {sum(digits)}')
