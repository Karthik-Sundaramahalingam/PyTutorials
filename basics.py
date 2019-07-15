numbers = [1, 3, 5, 7, 9]

numbers.append(2)
print(numbers)

names = ['apple', 'microsoft', 'google']
print(names[0].title())

for name in names:
    print(name.capitalize())

names.append('facebook')

names.insert(2, 'twitter')

names.sort()
print(names)
names.sort(reverse=True)
print(names)

del names[2]
print(names)

names.pop(1)
print(names)

names.remove('facebook')
print(names)

# String Strip

text = 'Is whitespace allowed?  '
print(f'Right Strip for: {text}')
print(text.rstrip())

text = '  In name of the kingdom..'
print(f'Left Strip for:{text}')
print(text.lstrip())

text = ' Valar Moghulis '
print(f'Stripping for the text: {text}')
print(text.strip())

# String Title case

text = 'once upon a time in mexico'
print(f'Title case for the text: {text}')
print(text.title())