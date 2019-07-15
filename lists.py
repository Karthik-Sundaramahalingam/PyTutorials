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