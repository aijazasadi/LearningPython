from collections import namedtuple

'''
LISTS
'''
fruits= ["apple", "banana", "cherry", "date"]

new_fruits = [
    ["apple", 1.2],
    ["banana", 0.5],
    ["cherry", 2.5],
    ["date", 3.0]
]
fruits_prices = [1.2, 0.5, 2.5, 3.0]
more_fruits_fruits = [
    fruits[0], fruits_prices[0],
    fruits[1], fruits_prices[1],
    fruits[2], fruits_prices[2],    
    ]
more_fruits = ["elderberry", "fig", "grape"]

# fruits += more_fruits
fruits = fruits + more_fruits
# fruits[2] = "citrus"
fruits.insert(2, "citrus")

fruits.sort()
fruits.reverse()
# print(*fruits, sep=f"\n")

fruits_tuple = ("apple", "banana", "cherry", "date")

fruits_list = list(fruits_tuple) # converting tuple to list
fruits_list.append("elderberry")

fruits_tuple = tuple(fruits_list) # converting list back to tuple

# print(fruits_tuple)
fruits.sort()
# print(*new_fruits, sep="\n")
# apple, banana, *rest = fruits_tuple
# print(apple)
# print(banana)
# print(type(rest)) 
Fruit = namedtuple("Fruit", ['name', 'price', 'quantity']) # named tuple

fruit1 = Fruit("apple", 1.2, 10)
fruit2 = Fruit("banana", 2.2, 20)

print(f"{fruit1.name}, {fruit1.price}, {fruit1.quantity}")
# print(fruit1)

program_to_continue = True

while(program_to_continue):
    user_input = input("Enter fruit name to search (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        program_to_continue = False
    else:
        if user_input in fruits:
            print(f"{user_input} is available.")
        else:
            print(f"{user_input} is not available.")