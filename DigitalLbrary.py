# #book_name
# book_name = input("Enter book name: ")

# #book_issue_date
# book_issue_date = input("Enter book issue date (dd-mm-yyyy): ")

# #book_author
# book_author = input("Enter book author: ")

# #book_ISBN
# #1-4028-9462-7
# book_ISBN = input("Enter book ISBN(#1-4028-9462-7): ")
# list of book names
book_names = ['Learn Python the Hard Way', 'Automate the Boring Stuff with Python', 'Python Crash Course', 'Fluent Python', 'Effective Python']
book_issue_dates = ['01-01-2020', '15-03-2021', '22-07-2019', '10-10-2018', '05-05-2022']
#output
# print(book_name , "," , book_issue_date , "," , book_author , "," , book_ISBN)
print("Available books in the library: ", *book_names, sep = ", ")