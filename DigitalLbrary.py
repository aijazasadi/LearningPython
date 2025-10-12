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
book_names = ['Learn Python the Hard Way', 'Automate the Boring Stuff with Python', 'Python Crash Course', 'Fluent Python', 'Effective Python']
book_issue_dates = ['01-01-2020', '15-03-2021', '22-07-2019', '10-10-2018', '05-05-2022']
#output
print("Available books in the library: ", *book_names, sep = ", ")