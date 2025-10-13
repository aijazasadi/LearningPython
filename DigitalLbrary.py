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
#output
# print("Available books in the library: ", *book_names, sep = ", ")
# print("Book 1 ", book_names[0])
# print("Total Books ", len(book_names))

input_book_index = int(input("Enter book index (0-4): "))


if(input_book_index >=0 or input_book_index < len(book_names)): 
    print("You have selected book: ", book_names[input_book_index])
    print("Book Author: ", book_authors[input_book_index])
    print("Book Issue Date: ", book_issue_dates[input_book_index])
    print("Book Return Date: ", book_return_dates[input_book_index])
else:
    print("Invalid book index")