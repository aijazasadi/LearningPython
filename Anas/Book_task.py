book_names = [
    'Why nations go to war', 
    'The Art Of War',
    'The Prince', 
    'On War', 
    'The 33 Strategies of War' 
]
book_issue_dates = [  # example dates
    '01-10-2025',
    '15-10-2025',
    '22-10-2025',
    '10-10-2025',
    '05-10-2025'
]
book_return_dates = [  # example dates
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

all_details = [book_names, book_issue_dates, book_return_dates, book_authors]

print("Welcome to my library system\n")

print("1. View Details Of All Books")
print("2. Check Availability Of Books")
print("3. Add a Book")   
print("4. Remove A Book")

choice = int(input("\nEnter your choice: "))

def get_safe_length():
    return min(len(book_names), len(book_authors), len(book_issue_dates), len(book_return_dates))


def search_book(to_search):
    found_books = []
    length = get_safe_length()
    for i in range(length):
        if to_search.lower() in book_names[i].lower() or to_search.lower() in book_authors[i].lower():
            found_books.append(i)
    return found_books if found_books else None


def print_book_details():
    print("\nAll Books in Library:\n")
    length = get_safe_length()
    for i in range(length):
        print(f"{book_names[i]} / {book_authors[i]} / {book_issue_dates[i]} / {book_return_dates[i]}")


def add_book():
    new_book_name = input("Enter new book name: ")
    new_book_author = input("Enter new book author: ")
    new_book_issue_date = input("Enter new book issue date (dd-mm-yyyy): ")
    new_book_return_date = input("Enter new book return date (dd-mm-yyyy): ")
    
    book_names.append(new_book_name)
    book_authors.append(new_book_author)
    book_issue_dates.append(new_book_issue_date)
    book_return_dates.append(new_book_return_date)
    
    print("✅ Book added successfully!")


def remove_book():
    remove_book_name = input("Enter book name to remove: ")
    if remove_book_name in book_names:
        index = book_names.index(remove_book_name)
        # Pop from all lists safely
        if index < get_safe_length():
            book_names.pop(index)
            book_authors.pop(index)
            book_issue_dates.pop(index)
            book_return_dates.pop(index)
            print("✅ Book removed successfully!")
        else:
            print("⚠️ Invalid index detected — lists may be unsynced.")
    else:
        print("❌ Book not found!")



if choice == 1:
    print_book_details()

elif choice == 2:
    search_input = input("Enter book name or author to search: ")  
    found_books = search_book(search_input)

    if found_books:
        print(f"\n✅ Found {len(found_books)} matching book(s):\n")
        for i in found_books:
            print(f"{book_names[i]} / {book_authors[i]} / {book_issue_dates[i]} / {book_return_dates[i]}")
    else: 
        print("❌ No matching books found.")

elif choice == 3:
    add_book()

elif choice == 4:
    remove_book()

else:
    print("Invalid choice.")


