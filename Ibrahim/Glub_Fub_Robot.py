#This robot will give you 1 of many random automated responses like 
import random

GlubFub_Storage = input("What do you want to ask Glub Fub(1-5):")
#Pascal Case but the second word starts with capital letter like Random_Gen
#camel case like randomGen
#snake case like random_gen
first_random_number = int(input("Enter a first number:"))
second_random_number = int(input("Enter a second number:"))

Random_gen = random.randrange(1, 5) 
random_number = random.randint(first_random_number, second_random_number)

if Random_gen == 1:
    print("Yes")

if Random_gen == 2:
    print("No")

if Random_gen == 3:
    print("Maybe...")

if Random_gen == 4:
    print("Definitely")

if Random_gen == 5:
    print("Never")

# Asad's random code
# you can use if-elif-else statement too
# or you can use match-case statement
if random_number % 2 == 0:
    print(f"The random number is {random_number}, which is an even number.")
else:  
    print(f"The random number is {random_number}, which is an odd number.")