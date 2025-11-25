from collections import namedtuple
from datetime import datetime
import operator
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
BOOK_COLS = ['name', 'issue_date', 'return_date', 'author', 'preface']

book = namedtuple("Book", BOOK_COLS)

zipped_books = zip(book_names, book_issue_dates, book_return_dates, book_authors, book_prefaces)

books = [book(name, issue_date, return_date, author, book_preface) for name, issue_date, return_date, author, book_preface in zipped_books]
books.sort() 
#function to print book details by index
def print_book_details(book):
    if(book in books):
        print("_" * 20)
        print("Book Name: ", book.name)
        print("Book Issue Date: ", book.issue_date)
        print("Book Return Date: ", book.return_date)
        print("Book Author: ", book.author)
    else:
        print("Invalid book ")

def print_books(books_to_be_printed):
    for book in books_to_be_printed:
        print_book_details(book)
        print("-" * 20)        
#printing all books
def print_all_books():
     for book in books:
        print_book_details(book)
        print("-" * 20)

def get_book(to_search, book_key):
    for book in books:
        if(to_search.strip().lower() in getattr(book, book_key).lower()):
            return book
    return None

def get_books(to_search, book_key):
    found_books = []
    for book in books:
        if(to_search.strip().lower() in getattr(book, book_key).lower()):
            found_books.append(book)
    return found_books

"""
    Search for books based on a date comparison.

    Args:
        max_date (str): The date to compare against in 'DD-MM-YYYY' format.
        date_field (str): The field name to compare (e.g., 'issue_date', 'return_date').
        comparison_operator (function): A function from the `operator` module (e.g., operator.le, operator.lt).

    Returns:
        list: Books matching the criteria.
      
    """
def get_books_by_date(date_to_compare, date_field, comparison_operator):
    
    date_to_compare_obj = datetime.strptime(date_to_compare, "%d-%m-%Y")  # Convert max_date to a datetime object
    found_books = []

    for book in books:
        date_to_search = datetime.strptime(getattr(book, date_field), "%d-%m-%Y")  # Convert book's date to datetime
        if comparison_operator(date_to_search, date_to_compare_obj):  # Use the passed operator for comparison
            found_books.append(book)

    return found_books

def update_book(book, book_arg, new_change):
    if book_arg in book._fields:  # Check if book_arg is a valid field name
        updated_book = book._replace(**{book_arg: new_change})  
        book_index = books.index(book) #find index of the old book
        books[book_index] = updated_book #replace with updated book
        books.sort()
        return updated_book
    else:
        print(f"Invalid book_arg: {book_arg}")
    

def delete_book(book_to_delete): #remove book from the books list (books.pop() will remove the last book)
    books.remove(book_to_delete)
    books.sort()
    

def add_book(new_book): #appends to the books list at the end
    books.append(new_book)
    books.sort()
    return new_book

current_book = get_book("Brett   ", "author") # should return Zed A. Shaw
# adding new book
new_book = book ("Deep Work", "12-12-2023", "12-01-2024", "Cal Newport", "Some preface about deep work.")
new_book = add_book(new_book)

updated_book = update_book(new_book, "author", "Asad Aijaz")
# print_book_details(updated_book)

# print_book_details(new_book)
# deleting current book
delete_book(current_book)

'''operator.le means less than or equal to <=
   operator.lt means less than <
   operator.ge means greater than or equal to >=
   operator.gt means greater than >
   operator.eq means equal to ==
   operator.ne means not equal to !=
   operator.contains means contains in
'''

found_books_bydate = get_books_by_date("10-10-2018", "return_date", operator.ge)
# print_books(found_books_bydate)
books_dict = {}
for book in books:
    book = {
        "book_name": book.name,
        "issue_date": book.issue_date,
        "return_date": book.return_date,
        "author": book.author,
        "preface": book.preface
    }
    books_dict[book["book_name"]] = book #using book name as key
# Print the dictionary

print(books_dict) #can be isbn if available
# print(books_dict.get('Learn Python the Hard Way'))
