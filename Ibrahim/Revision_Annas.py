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

"""
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rstrip()	Returns a right trim version of the string
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""

"""
count()	Returns the number of times a specified value occurs in a string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
join()	Joins the elements of an iterable to the end of the string
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
split()	Splits the string at the specified separator, and returns a list
rsplit()	Splits the string at the specified separator, and returns a list
title()	Converts the first character of each word to upper case

"""
print("--" * 20)

#Boolean
print("Boolean")

fat_man = 21
little_boy = 15

if fat_man > little_boy:
    print("That is a big bomb")
else: 
    print("That is a thin bomb")

print(bool("All is true until blank or 0 or none or false"))
# Leaving Functions

x = 200
print(isinstance(x, int))

print("--" * 20)

#Operators
print("Operators")

sum1 = 9 + 11
sum2 = sum1 + 1 

# + | - | * | / | % | ** Exponent | // Floor division | 
# Division returns a float where as Floor division a integer 

"""
= 
+=
-= 
*=
/=
%=
//=
**=
&=
|=
^=
>>=
<<=

"""
print(Neil:= "Genius")

"""
==
!=
>
<
>=
<=

"""
# (and) Returns True if both statements are true
# (or) Returns True if one of the statements is true
# (not) Reverse the result, returns False if the result is true
# (is) Returns True if both variables are the same object
# (is not) Returns True if both variables are not the same object
# (in) Returns True if a sequence with the specified value is present in the object
# (not in) Returns True if a sequence with the specified value is not present in the object

# Bitwise Operators (Go and Search up what they do Fatty)
# Operator Precedence (It is just like Python version of PEMDAS or BODMAS)

print("--" * 20)

#Lists
print("Lists")

#Store collections of Data
access_list = ["Sympathy", "Empathy", "Compassion", "Compassion"] #Indexed allow Dupes 
print(len(access_list)) #They are ordered and Changeable

# -1 to the len to find the index and a list can be any data type 

print(type(access_list)) #<class 'list'>
# list()

print(access_list[-3])
print(access_list[:3])

if "Empathy" in access_list:
    print("Are you blind ofcourse it is")

change_list = ["Change name", "Glorious model o", "Roccat kone pro", "Gpro superlight"]
change_list[0] = "The 0 mouse" # You can also use ranges  
print(change_list)

change_list.insert(2, "Bloody A40")
print(change_list)

add_list = ["Ajazz ak820 pro", "Alua F75", "Wooting 60he"]
add_list.append("Kisnt Kn85")
print(add_list) 

change_list.extend(add_list) #can be used in all data structures
print(change_list)  

remove_list = ["Random Chinese brand","Nvidia", "AMD", "Intel"]
remove_list.remove("Intel") # if there are 2 instances then it will remove the first one
print(remove_list)  

remove_list.pop(2) #if the index is not specified then .pop removes the last item
print(remove_list) 

del remove_list[0] #can also delete a whole list
print(remove_list) 

remove_list.clear() 
print(remove_list) 

#for loop
loop_list = ["Samsung", "MSI", "Asus", "Alienware"]

 # We are defining the range by len so we dont have to count and we define in len what list we want the lenght of.
for any_var in range(len(loop_list)): # We generally name any_var (i)
    print(loop_list[i])

#smallest for loop
[print(any_var) for any_var in loop_list]

#While loop 

while_list = ["Corshair", "Gskill", "Crutial", "Inland"]
any_var2 = 0 # you have to define this unlike for loops and this is also the index 
while any_var2 < len(while_list):
    print(while_list[any_var2])
    any_var2 = any_var2 + 1 #limiter