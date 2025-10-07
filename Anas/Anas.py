WELCOME="Welcome to Learning python on Vs"
print(WELCOME)

name1=input("Enter your name: ")
name2=input("Enter your name: ")

print(WELCOME, name1 , " and " , name2)

name1 = name2 
print(name1)

book_name = input("Enter book name: ")
#dd-mm-yyyy
book_issue_date = input("Enter book issue date: dd,mm,yyyy ")
#dd-mm-yyyy
book_return_date = input("Enter book return date: dd-mm-yyyy")
book_author = input("Enter book author: ")
book_genre = input("Enter book genre: ")
book_publisher = input("Enter book publisher: ")
book_language = input("Enter book language: ")
# 1-4028-9462-7
book_ISBN = int(input("Enter book ISBN: "))

print("Book name is: ", book_name, "Book author is:" , book_author , "Book genre is: ", book_genre, "Book publisher is: ", book_publisher, "Book language is: ", book_language, "Book ISBN is: ", book_ISBN)
print("You will issue this book by", book_issue_date, "You will return this book by", book_return_date)