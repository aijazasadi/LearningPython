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
    'Effective Python', #index 4
    'Python Tricks'  #index 5
]
book_issue_dates = ['01-01-2020', '15-03-2021', '22-07-2019', '10-10-2018', '05-05-2022', '12-12-2023']
book_return_dates = ['01-02-2020', '15-04-2021', '22-08-2019', '10-11-2018', '05-06-2022', '12-01-2024']
book_authors = ['Zed A. Shaw', 'Al Sweigart', 'Eric Matthes', 'Luciano Ramalho', 'Brett Slatkin', 'Zed A. Shaw']

# books =[
#     [book_names[0], book_issue_dates[0], book_return_dates[0], book_authors[0]], #[0][0]
#     [book_names[1], book_issue_dates[1], book_return_dates[1], book_authors[1]], #
#     [book_names[2], book_issue_dates[2], book_return_dates[2], book_authors[2]],
#     [book_names[3], book_issue_dates[3], book_return_dates[3], book_authors[3]],
#     [book_names[4], book_issue_dates[4], book_return_dates[4], book_authors[4]]
# ]   
books = []
for index, value in enumerate(book_names):
    books.append([book_names[index], book_issue_dates[index], book_return_dates[index], book_authors[index]])
books.sort()
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

def get_books(to_search, book_index):
    found_books = []
    for book in books:
        if(to_search.strip().lower() in book[book_index].lower()):
            found_books.append(book)
    return found_books

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

books = tuple(books)
books = list(books)

# add_book(["Python Tricks", "12-12-2023", "12-01-2024", "Dan Bader"])
print(*books, sep="\n")
# print(get_books("a. shaw", AUTHORS))

# books = list(books_tuple)

# print(type(books_tuple[2]))

books[2][BOOK_NAMES] = "Modified Title"


# print(books_tuple[2])
# count = 0

# while count < len(books_tuple):
#     print(books_tuple[count])
#     count += 1

# for index, book in enumerate(books_tuple):
#     print(f"Index {index}: {book}")

# for index in range(len(books_tuple)):
#     print(f"Index {index}: {books_tuple[index]}")   
# print(*books, sep="\n")
# returned_book = books[books.index(new_book)]
# print(returned_book)



