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
    "apple" : {
        "price_per_kg" : 5,
        "quantity_in_kg" : 10,
        "is_stock_available" : True
        },
    "banana" : {
        "price_per_kg" : 2,
        "quantity_in_kg" : 20,
        "is_stock_available" : True
        },
    "cherry" : {
        "price_per_kg" : 15,
        "quantity_in_kg" : 5,
        "is_stock_available" : False
        }
}


# index_apple = fruit_dict["fruit_name"].index("apple")
# print(fruit_dict["fruit_name"][index_apple])  # Accessing value by key
# print(fruit_dict["price_per_kg"][index_apple])  # Accessing value by key

is_apple_in_stock = False

if(fruit_dict["apple"] ):
    is_apple_in_stock = True

print("_" * 20)
for key, value in fruit_dict.items():
    print(f"{key}: {value}")
#message = f"Hello, my name is {name}, I am {age} years old, and I live in {city}."
message = f"Banana Status {fruit_dict['banana']['is_stock_available']}"
print(message)

#updating banana stock
fruit_dict["banana"]["price_per_kg"] = 2.5