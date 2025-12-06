# Creating a dictionary for borrowers
borrowers = {
    'C12345': {
        'name': 'Anas Ahmed',
        'book_issued_name': 'The Great Gatsby',
        'issue_date': '01-09-2023',
        'return_date': '01-10-2023'
    },
    'C23456': {
        'name': 'Bilal Khan',
        'book_issued_name': '1984',
        'issue_date': '05-09-2023',
        'return_date': '05-10-2023'
    },
    'C34567': {
        'name': 'Catherine Lee',
        'book_issued_name': 'To Kill a Mockingbird',
        'issue_date': '10-09-2023',
        'return_date': '10-10-2023'
    },
    'C45678': {
        'name': 'David Smith',
        'book_issued_name': 'Pride and Prejudice',
        'issue_date': '15-09-2023',
        'return_date': '15-10-2023'
    },
    'C56789': {
        'name': 'Eva Johnson',
        'book_issued_name': 'On War',
        'issue_date': '20-09-2023',
        'return_date': '20-10-2023'
    }
}

# Search functionality
to_search = "de "

found = False
for card_number, borrower in borrowers.items():
    if to_search.lower().strip() in borrower['book_issued_name'].lower():  # Access by key
        print("Found")
        print("_" * 20)
        print(f"Card Number: {card_number}")
        for key, value in borrower.items():  # Iterate for better readability
            print(f"{key}: {value}")
        found = True
        break

if not found:
    print("No matching book found.")

print("_" * 20)
print(borrowers['C12345'])
