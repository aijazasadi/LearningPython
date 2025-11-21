# #This is a file where i will write my own code

# #decleration
# Welcome_message = "Welcome to Learning python on Visual studios "

# #input
# participant_1 = input("Enter your name: ")
# participant_2 = input("Enter your name: ")
# teacher_1 = input("Enter your teacher's name: ")

# #output
# print(Welcome_message + participant_1 + " and " + participant_2 + " you are learning Python with " + teacher_1)

# """
# This is a multi-line comment that i learned so i put it here 
# to remember it
# """


#legal variable names
#constant variable usually in uppercase
#participant_1 = participant_2 overwrite
#write cls to clear the terminal
#print("Annas" == "Annas")
#type casting
#the type of variable 
#multi line string
#lists 
#mixed Lists
#sep = " / "
#multi dimentional array or lists 
#index 
#len fuction
#if statement
#Functions (def name():)
#f or inline comment
#.strip()
#.lower()
#for loop
#range()
#function with return value
#in function
#join as a caracter
#.capitalize()
#.upper()
#.swapcase()
#reverse()
#Class (Constant not fully studied yet)
#Basic Constants 
#.append()
#.pop()
#.remove()
#.sort()
#tuple ("Anything",)
#while 
#enumerate()
#zip
#del 

from collections import namedtuple
import operator

CONSTANT = 10  # This is a constant variable meaning it should not be changed

#Tuple example
tuple_example = ("Tuples can not be changed and have a difinitve order", "And they allow for duplicate values", "They can be any data type",  "This is to be replaced")
tuple_list = list(tuple_example) 
tuple_list.append("you can update tuples by making them a list first")
tuple_example = tuple(tuple_list)

#Getting length of tuple
length_of_tuple = len(tuple_example)

#Named Tuple example
var_example1 = ["Write anything here"]
var_example2 = ["Write something different here"]

examplelist = namedtuple("examplelist", ["var_example1", "var_example2"])
convertback = examplelist(var_example1, var_example2)

#function example
def function_example(function_arg1, function_arg2):
    print("This is an example function", function_arg1, function_arg2)
    return None

#zip example
a = ("Annas" )
b = ("Ibrahim")
zipped = zip(a, b)

#printing examples
print(tuple_example[0:5]) 
print(convertback.var_example1) 
function_example("this is arg1", "this is arg2")
print("The length of the tuple is:", length_of_tuple)
print(tuple(zipped))



#Inworking
operator_example = operator.add(5, 10)
print("The operator example adds 5 and 10 to make:", operator_example)
