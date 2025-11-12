from collections import namedtuple
from datetime import datetime
#constants for book details indices
BOOK_NAMES = 0
ISSUE_DATES = 1
RETURN_DATES = 2
AUTHORS = 3 

# list of book names
book_names = [
    'Learn Python the Hard Way', # index 0
    'Automate the Boring Stuff with Python', #index 1
    'Python Crash Course', #index 2
    'Fluent Python', #index 3
    'Effective Python', #index 4
    'Python Tricks'  #index 5
]
book_issue_dates = ['01-01-2020', '15-03-2021', '22-07-2019', '10-10-2018', '05-05-2022', '12-12-2023']
book_return_dates = ['01-02-2020', '15-04-2021', '22-08-2019', '10-11-2018', '05-06-2022', '12-01-2024']
book_authors = ['Zed A. Shaw', 'Al Sweigart', 'Eric Matthes', 'Luciano Ramalho', 'Brett Slatkin', 'Zed A. Shaw']

# Example multiline book prefaces
book_prefaces = [
    """This book is a beginner's guide to learning Python programming.
It provides step-by-step instructions and exercises to help you master the basics.""",
    """This book teaches you how to automate everyday tasks using Python.
It is perfect for office workers, students, and anyone who wants to save time.""",
    """This book is a hands-on guide to learning Python programming.
It includes practical projects to help you build real-world skills.""",
    """This book dives deep into Python's advanced features.
It is ideal for experienced programmers who want to write more efficient code.""",
    """This book provides tips and tricks for writing clean and effective Python code.
It is a must-read for Python developers who want to improve their skills."""
]

books = []

book = namedtuple("Book", ['name', 'issue_date', 'return_date', 'author', 'book_preface'])

zipped_books = zip(book_names, book_issue_dates, book_return_dates, book_authors, book_prefaces)

books = [book(name, issue_date, return_date, author, book_preface) for name, issue_date, return_date, author, book_preface in zipped_books]
books.sort()
#function to print book details by index
def print_book_details(book):
    if(book in books):
        print("Book Name: ", book[BOOK_NAMES])
        print("Book Issue Date: ", book[ISSUE_DATES])
        print("Book Return Date: ", book[RETURN_DATES])
        print("Book Author: ", book[AUTHORS])
    else:
        print("Invalid book ")
        
#printing all books
def print_all_books():
     for book in books:
        print(f"Details of Book {book}:")
        print_book_details(book)
        print("-" * 20)

def get_book(to_search, book_index):
    for book in books:
        if(to_search.strip().lower() in book[book_index].lower()):
            return book
    return None

def get_books(to_search, book_index):
    found_books = []
    for book in books:
        if(to_search.strip().lower() in book[book_index].lower()):
            found_books.append(book)
    return found_books

def update_book(book, book_arg, new_change):
    # replace will return a new namedtuple with the updated field
    if(book_arg == AUTHORS):
        updated_book = book._replace(author=new_change)
    elif(book_arg == BOOK_NAMES):
        updated_book = book._replace(name=new_change)
    elif(book_arg == ISSUE_DATES):
        updated_book = book._replace(issue_date=new_change)
    elif(book_arg == RETURN_DATES):
        updated_book = book._replace(return_date=new_change)
    elif(book_arg == 4): # book_preface
        updated_book = book._replace(book_preface=new_change)

    book_index = books.index(book) #find index of the old book
    books[book_index] = updated_book #replace with updated book
    books.sort()

def delete_book(book_to_delete): #remove book from the books list (books.pop() will remove the last book)
    books.remove(book_to_delete)
    books.sort()
    

def add_book(new_book): #appends to the books list at the end
    books.append(new_book)
    books.sort()

current_book = get_book("Brett   ", AUTHORS) # should return Zed A. Shaw

new_book = book ("Deep Work", "12-12-2023", "12-01-2024", "Cal Newport", "Some preface about deep work.")
add_book(new_book)
# print(current_book)

delete_book(current_book)
update_book(new_book, AUTHORS, "Asad Aijaz")



