from collections import namedtuple
import operator

'''
LISTS
'''
fruits= ["apple", "banana", "cherry", "date"]
operations = namedtuple("Operations", ['add', 'subtract', 'multiply', 'divide'])
ops = operations(add='add', subtract='subtract', multiply='multiply', divide='divide')

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

my_fruits = {'apple', 'banana', 'cherry'}
more_fruits = {'apple', 'fig', 'grape'}
some_more_fruits = ['banana', 'cherry', 'date']

# common_fruit = my_fruits.intersection(more_fruits)  # Intersection

# my_fruits = my_fruits | more_fruits   # Union
# my_fruits.update(some_more_fruits)  # Union with list

# my_fruits = my_fruits - more_fruits
my_fruits = my_fruits.symmetric_difference(more_fruits)  # Difference

# print(common_fruit)  # True])
# print(my_fruits)

fruit_dict = {
    "fruit_name" : [
        "apple",
        "banana",
        "cherry"
    ],
    "price_per_kg" : [1.2, 2.2, 3.5],
    "quantity_in_kg" : [10, 20, 15],
    "stock_available" : True
}


index_apple = fruit_dict["fruit_name"].index("apple")
print(fruit_dict["fruit_name"][index_apple])  # Accessing value by key
print(fruit_dict["price_per_kg"][index_apple])  # Accessing value by key