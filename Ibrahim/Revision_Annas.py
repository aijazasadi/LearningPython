"""termanologies 
Indentation is the space used to show hierarchy in control structures'
Statements are the instructions that are given to the computor program """


#Print
print("Print statement")

print("Teach me the print statment")
print('you can use singel commas \n And use the slash n to put in to different line')

print("Hello World!", end=" ")
print("I will print on the same line.")
print(0 + 2, "You can do this too")  

print("--" * 20)

#Variables
print("Variables")

var = "luv"
print("i", var, "python")

var1 = 2
var2 = 4
print(var1 + var2)

#global var
x = "This is a sequence"

def myfunc():
    # make y into global
    global y
    #local var
    y = "sequence this is"

myfunc()
print(y)   

"""
Camel case: myVariableName = "John Wick"
Pascal case: MyVariableName = "John Wick"
Snake case:my_variable_name = "John Wick" 

Cant add numbers, (-) or space
"""

print("--" * 20)

#Input
print("Inputs")

storage = input("Whatever:")

number_storage = int(input("Type a integer:"))
print(type(number_storage))

print("--" * 20)

#Data Types
print("Data Types")

a = 2 #int
b = "Annas" #str
c = True #bool
d = 3.14 #float
e = 1j #complex idk
f = ["Graple", "Banagnum", "chgrry"] #list
g = ("Graple", "Banagnum", "chgrry") #tuple
h = range(6) #range
i = {"name" : "John", "age" : 36} #dict
j = {"Graple", "Banagnum", "chgrry"} #set
k = frozenset({"Graple", "Banagnum", "chgrry"}) #frozenset
l = b"Hello" #bytes
m = bytearray(5) #bytearray  
n = memoryview(bytes(5)) #memort view
o = None #nonetype

print(a)
print(type(a))

print("--" * 20)

#Type Casting
# str/float/int

#Lists
print("Lists")
example_list = ["Muhammad", "Ibrahim"]
a, b = example_list
print(a + b); print(a, b)

print("--" * 20)

#Random Number
print("Random")
import random
print(random.randrange(1, 10))

#Python Strings
print("Strings")
print("'You can add quotes to the print like this'")

mls = """Multi 
line 
string"""

calling = "Osama Bin Laden"
print(calling[0:4])

for Looping in "Loop":
    print(Looping)

print(len(calling))

txt = "Serotonin is called the mother of all chemicals"
to_find = "chemicals"
print(to_find in txt)
print(to_find not in txt)

#.lower() all to lower
#.upper() ALL TO UPPER
#.strip() removes unwanted spaced
replaced = "P & G"
print(replaced.replace("&", "and"))

splitter = "Every End"
print(splitter.split("/")) 

#a + b = c

keys = 82 
print(f"there are {keys} on a keyboard")
print(f"there are {keys:2f} on a keyboard")# u can also perform math functions 

print("The new hardest level in \"gd\" is called greif")

print("It\'s")
print("He\\she")
print("Different \n line")
print("This \r Delete")
print("Tab\t?")
print("Backspaces\b")
#\f
print("\x48\x65\x6c\x6c\x6f") #This will say hello hex value
print("\110\145\154\154\157") #This will also say hello in octal value

print("--" * 20)

