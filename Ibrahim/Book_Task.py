# Make a list of books, book authors, book genres. Say 5 books 
# Print using print and sep syntax we learned
# try fetching book 3 or 4 along with authors, genre and related information remember the first book __index stats with 0__ 


book_name = ["Atomic Habits", "Breif history of Time", "Breif awnsers to big Questions", "Astrophysics for people in a Hurry", "Sun Zu Art of War"]
authors_name = ["James Clear", "Stephen Hawking", "Stephen Hawking", "Neil deGrasse Tyson", "Sun Tzu"]
genres_names = ["Self-help", "Science", "Science", "Science", "Military Strategy"]


book_number = int(input("Which book details do you want to see?: "))


if book_number >=0 and book_number < len(book_name):
    print (book_name[int(book_number)] , authors_name[int(book_number)] , genres_names[int(book_number)], sep= " / ")
else:
    print("Invalid book number")

    