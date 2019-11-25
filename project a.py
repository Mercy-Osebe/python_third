num_1 = input("Enter the first number:")
num_2 = input("enter another number")
result = float(num_1) + float(num_2)
print(result)
from math import *
friends =["mercy", "mike", "vic", "liam", "hope", "peace", "ray"]
my_numbers = [1, 2, 5, 4, 16, 25, 80, 5, 4]
friends.extend(my_numbers)
print(friends)
friends.append("mary")
print(friends)
friends.insert(4, "caro")
print(friends)
friends.remove("mercy")
print(friends)
friends.pop()
print(friends)

print(friends.count(4))
friends.reverse()
print(friends)

friends[4:]
print(friends[4:])
friends[4:10]
print(friends[4:10])
friends.clear()
print(friends)
my_numbers = [1, 2, 5, 4, 16, 25, 80, 5, 4]
my_numbers2 = my_numbers.copy()
print(my_numbers2)

print(my_numbers)
my_numbers.sort()
print(my_numbers)
my_numbers.count(4)
print(my_numbers.count(4))

