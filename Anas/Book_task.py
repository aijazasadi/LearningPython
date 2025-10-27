book_names = [
    'Why nations go to war', 
    'The Art of War',
    'The Prince', 
    'On War', 
    'The 33 Strategies of War' 
]
book_issue_dates = [ #example dates
    '01-10-2025',
    '15-10-2025',
    '22-10-2025',
    '10-10-2025',
    '05-10-2025'
]
book_return_dates = [ #example dates
    '21-10-2026',
    '15-12-2026',
    '22-11-2026',
    '10-11-2026',
    '05-12-2026'
]
book_authors = [
    'John G. Stoessinger',
    'Sun Tzu',
    'Niccolò Machiavelli',
    'Robert Greene',
    'Carl von Clausewitz'
]

books = [
    book_names,
    book_issue_dates,
    book_return_dates,
    book_authors
]




"""
if(input_book_index >=0 or input_book_index < len(book_names)): 
    print("You have selected book: ", book_names[input_book_index])
    print("Book Author: ", book_authors[input_book_index])
    print("Book Issue Date: ", book_issue_dates[input_book_index])
    print("Book Return Date: ", book_return_dates[input_book_index])
else:
    print("Invalid book index")
"""
all_details = [book_names, book_issue_dates, book_return_dates, book_authors]


print("welcome to my library system")

print("1. View Details Of Books")
print("2. Check Availability Of Books")
print("3. Remove A Book")   
print("4. Add A Book")

choice = int(input("Enter your choice: "))


def search_book(to_search, book_index):
    for book in range(len(all_details)):
        if to_search.lower() in all_details[book_index][book].lower():
            return all_details
    return None


def print_book_details():
 print(book_names)
 input_book_index = int(input("Enter book index (0-4): "))
 if input_book_index >=0 and input_book_index < len(book_names):
    print (book_names[int(input_book_index)] , book_authors[int(input_book_index)] , book_issue_dates[int(input_book_index)] , book_return_dates[int(input_book_index)],  sep= " / " )
 else:
    print("Invalid book number")


if choice == 1:
    
    print_book_details()

if choice == 2:
    print(book_names)
    print("Check Availability Of Books")
search_input = input("Search book details:")  

if search_book(search_input, book_index=0):
    print("Found", search_input, "in the book details.")
else: 
    print(search_input, "not found in the book details.")
