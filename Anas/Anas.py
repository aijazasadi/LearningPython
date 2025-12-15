from datetime import datetime;
from datetime import timedelta;
WELCOME="Welcome to Learning python on Vs"
print(WELCOME)

# name1=input("Enter your name: ")
# name2=input("Enter your name: ")

# print(WELCOME, name1 , " and " , name2)

# name1 = name2 
# print(name1)

# book_name = input("Enter book name: ")
#dd-mm-yyyy
book_issue_date = input("Enter book issue date: dd-mm-yyyy ")
print("Type of book_issue_date",type(book_issue_date))

day, month, year = book_issue_date.split('-')
print("Day:", day, "Month:", month, "Year:", year)
print("Type of day:",type(day)) #still string
print("Type of month:",type(month))
print("Type of year:",type(year))

day = int(day)
month = int(month)
year = int(year)

print("\nType of day:",type(day)) # now integer
print("Type of month:",type(month))
print("Type of year:",type(year))

print(day+14) # we are adding 14 days to the day of issue
print("New return date will be:", day+14, "-", month, "-", year) 
#seems fun but what wil happen if we input 25-12-2023

date_object = datetime.strptime(book_issue_date, "%d-%m-%Y")
day = date_object.day
month = date_object.month
year = date_object.year

print("Type of date_object:",type(date_object))
return_date_object = date_object + timedelta(days=14)
return_date_object =return_date_object.__format__("%d-%m-%Y")
print("Return date object:", return_date_object)    


#dd-mm-yyyy
# book_return_date = input("Enter book return date: dd-mm-yyyy")
# book_author = input("Enter book author: ")
# book_genre = input("Enter book genre: ")
# book_publisher = input("Enter book publisher: ")
# book_language = input("Enter book language: ")
# # 1-4028-9462-7
# book_ISBN = int(input("Enter book ISBN: "))

# print("Book name is: ", book_name, "Book author is:" , book_author , "Book genre is: ", book_genre, "Book publisher is: ", book_publisher, "Book language is: ", book_language, "Book ISBN is: ", book_ISBN)
# print("You will issue this book by", book_issue_date, "You will return this book by", book_return_date)