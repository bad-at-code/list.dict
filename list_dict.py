"""hello."""
print("Dictionary")
dict = {1: 'Example', 2: 'Example2', 3: 'Example3'}
print(dict)

print()
print()

print("Appending the Dictionary")
dict[4] = 'Example4'
print(dict)

print()
print()

print("Finding a part of the Dictionary")
print(dict[1])

print()
print()

print("Deleting a part of a Dictionary")
del dict[2]
print(dict)

print()
print("-------------------")
print()
# Making the list
list = ['test', 'test2', 'test3']
print(list)

print("Appending the lsit")

print("Finding a part of the list")
list.insert(3, 'test4')

print("Deleting a part of the list")
list.pop(1)
