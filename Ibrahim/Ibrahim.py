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
#tuple
#while 
#enumerate()
#zip

from DigitalLbrary import AUTHORS, BOOK_NAMES, ISSUE_DATES, RETURN_DATES, book_names, book_issue_dates, book_return_dates, book_authors, book_prefaces

from collections import namedtuple
from datetime import datetime

books = []
book = namedtuple("Book", ['name', 'issue_date', 'return_date', 'author', 'book_preface'])
zipped_books = zip(book_names, book_issue_dates, book_return_dates, book_authors, book_prefaces)

books = [book(name, issue_date, return_date, author, book_preface) for name, issue_date, return_date, author, book_preface in zipped_books]
books.sort() 

print(books, sep="\n")