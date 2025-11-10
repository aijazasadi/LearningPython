book_names = [
    'Why nations go to war',
    'The Art Of War',
    'The Prince',
    'On War',
    'The 33 Strategies of War'
]

book_issue_dates = [
    '01-10-2025',
    '15-10-2025',
    '22-10-2025',
    '10-10-2025',
    '05-10-2025'
]

book_return_dates = [
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

books = [book_names, book_issue_dates, book_return_dates, book_authors]
all_details = [book_names, book_issue_dates, book_return_dates, book_authors]

print("welcome to my library system")
print("1. View Details Of Books")
print("2. Check Availability Of Books")
print("3. Add a Book")
print("4. Remove A Book")

choice = int(input("Enter your choice: "))

def search_book(to_search, book_index):
    for book in range(len(all_details)):
        if to_search.lower() in all_details[book_index][book].lower():
            return all_details
    return None

def print_book_details():
    print(book_names)
    input_book_index = int(input("Enter book index (0-4): "))

    if input_book_index >= 0 and input_book_index < len(book_names):
        print(
            book_names[input_book_index],
            book_authors[input_book_index],
            book_issue_dates[input_book_index],
            book_return_dates[input_book_index],
            sep=" / "
        )
    else:
        print("Invalid book number")

def add_book():
    new_book_name = input("Enter new book name: ")
    new_book_author = input("Enter new book author: ")
    new_book_issue_date = input("Enter new book issue date (dd-mm-yyyy): ")
    new_book_return_date = input("Enter new book return date (dd-mm-yyyy): ")

    book_names.append(new_book_name)
    book_authors.append(new_book_author)
    book_issue_dates.append(new_book_issue_date)
    book_return_dates.append(new_book_return_date)

    print("Book added successfully!")

def remove_book():
    remove_book_name = input("Enter book name to remove: ")
    if remove_book_name in book_names:
        index = book_names.index(remove_book_name)
        book_names.pop(index)
        book_authors.pop(index)
        book_issue_dates.pop(index)
        book_return_dates.pop(index)
        print("Book removed successfully!")
    else:
        print("Book not found!")

while True:
    if choice == 1:
        print_book_details()

    if choice == 2:
        print(book_names)
        print("Check Availability Of Books")
        search_input = input("Search book details: ")
        if search_book(search_input, book_index=0):
            print("Found", search_input, "in the book details.")
        else:
            print(search_input, "not found in the book details.")

    if choice == 3:
        print(book_names)
        add_book()

    if choice == 4:
        print(book_names)
        remove_book()
        print(book_names)

    cont = input("Do you want to continue? (yes/no): ")
    if cont.lower() == "no":  
        break

    choice = int(input("Enter your choice: "))  
