#constants for book details indices
BOOK_NAMES = 0
ISSUE_DATES = 1
RETURN_DATES = 2
AUTHORS = 3 

# list of book names
#length book
book_names = [
    'Learn Python the Hard Way', # index 0
    'Automate the Boring Stuff with Python', #index 1
    'Python Crash Course', #index 2
    'Fluent Python', #index 3
    'Effective Python' #index 4
]
book_issue_dates = ['01-01-2020', '15-03-2021', '22-07-2019', '10-10-2018', '05-05-2022']
book_return_dates = ['01-02-2020', '15-04-2021', '22-08-2019', '10-11-2018', '05-06-2022']
book_authors = ['Zed A. Shaw', 'Al Sweigart', 'Eric Matthes', 'Luciano Ramalho', 'Brett Slatkin']

books=[book_names, book_issue_dates, book_return_dates, book_authors]

books = [book_names[0], book_issue_dates[0], book_return_dates[0], book_authors[0]]

books =[
    [book_names[0], book_issue_dates[0], book_return_dates[0], book_authors[0]], #[0][0]
    [book_names[1], book_issue_dates[1], book_return_dates[1], book_authors[1]], #
    [book_names[2], book_issue_dates[2], book_return_dates[2], book_authors[2]],
    [book_names[3], book_issue_dates[3], book_return_dates[3], book_authors[3]],
    [book_names[4], book_issue_dates[4], book_return_dates[4], book_authors[4]]
]   

#function to print book details by index
def print_book_details(book):
    books.sort()
    if(book in books):
        print("Book Name: ", book[BOOK_NAMES])
        print("Book Issue Date: ", book[ISSUE_DATES])
        print("Book Return Date: ", book[RETURN_DATES])
        print("Book Author: ", book[AUTHORS])
    else:
        print("Invalid book ")
        
#printing all books
def print_all_books():
     books.sort()
     for book in books:
        print(f"Details of Book {book}:")
        print_book_details(book)
        print("-" * 20)

def get_book(to_search, book_index):
    for book in books:
        if(to_search.strip().lower() in book[book_index].lower()):
            return book
    return None

def update_book(book, book_arg, new_change):
    book[book_arg] = new_change
    books.sort()
    
def delete_book(bookToDelete): #remove book from the books list (books.pop() will remove the last book)
    books.remove(bookToDelete)
    books.sort()

def add_book(new_book): #appends to the books list at the end
    books.append(new_book)
    books.sort()

current_book = get_book("Brett   ", AUTHORS) # should return Zed A. Shaw
# print_book_details(current_book)

new_book = ["Deep Work", "12-12-2023", "12-01-2024", "Cal Newport"]

# update_book(current_book, BOOK_NAMES, "Changed Book Title")

add_book(new_book)
# print(*books, sep="\n")
print_all_books()
