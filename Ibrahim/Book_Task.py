# Make a list of books, book authors, book genres. Say 5 books 
# Print using print and sep syntax we learned
# try fetching book 3 or 4 along with authors, genre and related information remember the first book __index stats with 0__ 


Books = ["Atomic Habits", "Breif history of Time", "Breif awnsers to big Questions", "Astrophysics for people in a Hurry", "Sun Zu Art of War"]
Authors = ["James Clear", "Stephen Hawking", "Stephen Hawking", "Neil deGrasse Tyson", "Sun Tzu"]
Genres = ["Self-help", "Science", "Science", "Science", "Military Strategy"]


book_number = (input("Which book details do you want to see?: "))

print (Books[int(book_number)] , Authors[int(book_number)] , Genres[int(book_number)], sep= " / ") 

if(book_number >=0 or book_number < len(Books)):
    print("You have selected book: ", Books[int(book_number)])
    print("Book Author: ", Authors[int(book_number)])
    print("Book Genre: ", Genres[int(book_number)])
else:
    print("Invalid book index") 




# Incomplete code above i dont know how to fetch 3rd or 4th book with related information yet

# print(Books[0] , Authors[0] , Genres[0], sep= " / ")
#print(Books[1] , Authors[1] , Genres[1], sep= " / ")
#print(Books[2] , Authors[2] , Genres[2], sep= " / ")
#print(Books[3] , Authors[3] , Genres[3], sep= " / ")