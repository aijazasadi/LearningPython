#This robot will give you 1 of many random automated responses like 
import random

GlubFub_Storage = input("What do you want to ask Glub Fub:")

Random_gen = random.randrange(1, 5)

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