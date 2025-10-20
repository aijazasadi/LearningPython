#book_name
#dd-mm-yyyy
#book_issue_date
#dd-mm-yyyy
#book_return_date
#book_author
#book_genre
#book_publisher
#book_language
# 1-4028-9462-7
#book_ISBN


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

# print(books[0][3])

#function to print book details by index
def print_book_details(index):
    if index >= 0 and index < len(books):
        print("Book Name: ", books[index][0])
        print("Book Issue Date: ", books[index][1])
        print("Book Return Date: ", books[index][2])
        print("Book Author: ", books[index][3])
        print("*" * 20)
    else:
        print("Invalid book index")
#printing all books
def print_all_books():
    for book in range(len(books)):
        print(f"Details of Book {book}:")
        print_book_details(book)
        print("-" * 20)

def get_book_by_name(book_name, index):
    for book in range(len(books)):
        # print(book_name.strip().lower() in books[book][0].strip().lower())
        if books[book][0].strip().lower() in book_name.strip().lower(): #map book by title
            return books[book][index]
    return None
# input_book_index = int(input("Enter book index (0-4): "))
# print_all_books()

def change_book(new_book_name, book_index):
    if book_index >= 0 and book_index < len(books):
        books[book_index][0] = new_book_name
    else:
        print("Invalid book index")   

# print(get_book_by_name("Python the Hard Way", 0)) # should return Zed A. Shaw

# print('\n'.join([str(item) for item in books]))
