# Make a list of books, book authors, book genres. Say 5 books 
# Print using print and sep syntax we learned
# try fetching book 3 or 4 along with authors, genre and related information remember the first book __index stats with 0__ 

#Default book lists
book_name = ["Atomic Habits", "Breif history of Time", "Breif awnsers to big Questions", "Astrophysics for people in a Hurry", "Sun Zu Art of War"]
authors_name = ["James Clear", "Stephen Hawking", "Stephen Hawking", "Neil deGrasse Tyson", "Sun Tzu"]
genres_names = ["Self-help", "Science", "Science", "Science", "Military Strategy"]
all_details = [book_name, authors_name, genres_names]

#Add a book 
def add_book():
    new_book_name = input("Enter new book name: ")
    new_book_author = input("Enter new book author: ")
    new_book_genre = input("Enter new book genre: ")

    book_name.append(new_book_name)
    authors_name.append(new_book_author)
    genres_names.append(new_book_genre)

    print("Book added successfully!")

#search book details by index function
def print_book_details():
 if book_number >=0 and book_number < len(book_name):
    print (book_name[int(book_number)] , authors_name[int(book_number)] , genres_names[int(book_number)], sep= " / " )
 else:
    print("Invalid book number")

#search book by name
def search_book(to_search, book_index):
    for book in range(len(all_details)):
        if to_search.strip().lower() in all_details[book_index][book].lower():
            return all_details
    return None

#input and search book by name
search_input = input("Search book details:")  
if search_book(search_input, book_index=0):
    print("Found", search_input, "in the book details.")
else: 
    print(search_input, "not found in the book details.")

#Prototype book add
add_book()

#input index search 
book_number = int(input("Which book details do you want to see?: "))
print_book_details()