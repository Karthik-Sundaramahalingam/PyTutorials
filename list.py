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