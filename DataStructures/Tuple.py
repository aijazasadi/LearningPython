# Import the namedtuple library for the second part of the example

# Data lists remain the same
names = ['Anas Ahmed', 'Bilal Khan', 'Catherine Lee', 'David Smith', 'Eva Johnson']
card_numbers = ['C12345', 'C23456', 'C34567', 'C45678', 'C56789']
book_issued_names = ['The Great Gatsby', '1984', 'To Kill a Mockingbird', 'Pride and Prejudice', 'On War']
issue_dates = ['01-09-2023', '05-09-2023', '10-09-2023', '15-09-2023', '20-09-2023']
return_dates = ['01-10-2023', '05-10-2023', '10-10-2023', '15-10-2023', '20-10-2023']

# Convert the master list to store tuples instead of lists
borrowers = []

if(len(names) == len(card_numbers) == len(book_issued_names) == len(issue_dates) == len(return_dates)):
    print("All lists are of equal length. Proceeding to create borrower records.")
    number_of_borrowers = len(names)

    for i in range(number_of_borrowers):
        # A record is now a tuple () instead of a list []
        borrower_record = (
            names[i],
            card_numbers[i],
            book_issued_names[i],
            issue_dates[i],
            return_dates[i]
        )
        borrowers.append(borrower_record)

print("\n--- Tuple Records Created ---")
print(*borrowers, sep="\n")

# ---------------------------------------------------
# ADD Functionality (Tuples)
# ---------------------------------------------------
def add_borrower(name, card_num, book_name, issue_d, return_d):
    new_record = (name, card_num, book_name, issue_d, return_d)
    borrowers.append(new_record)
    print(f"\nAdded new borrower: {name}")

add_borrower('Frank Adams', 'C67890', 'Dune', '25-09-2023', '25-10-2023')

# ---------------------------------------------------
# DELETE Functionality (Tuples)
# ---------------------------------------------------
def delete_borrower_by_card(card_number_to_delete):
    global borrowers # Ensure we modify the global borrowers list
    # Filter creates a new list excluding the matching record
    borrowers = [record for record in borrowers if record[1] != card_number_to_delete]
    print(f"\nDeleted borrower with card number: {card_number_to_delete}")

delete_borrower_by_card('C12345') # Deletes Anas Ahmed

# ---------------------------------------------------
# UPDATE Functionality (Tuples)
# ---------------------------------------------------
def update_book_name(card_number_to_find, new_book_name):
    for i, record in enumerate(borrowers):
        if record[1] == card_number_to_find: # card_number is at index 1
            # Tuples are immutable. We must create a NEW tuple with the updated value
            # and replace the old one in the list.
            updated_record = (record[0], record[1], new_book_name, record[3], record[4])
            borrowers[i] = updated_record
            print(f"\nUpdated book for {record[0]} to '{new_book_name}'")
            return
    print(f"\nCard number {card_number_to_find} not found for update.")

update_book_name('C23456', 'The Hitchhiker\'s Guide to the Galaxy')

# ---------------------------------------------------
# SEARCH Functionality (Original Code Integrated)
# ---------------------------------------------------
to_search = "the "
print(f"\n--- Searching for books containing '{to_search.strip()}' ---")

found_count = 0
for borrower in borrowers:
    # Use index 2 for book_issued_name
    if to_search.lower().strip() in borrower[2].lower():
        print("Found")
        print("_" * 20)
        print(f"Name: {borrower[0]}\nCard: {borrower[1]}\nBook: {borrower[2]}\nIssue: {borrower[3]}\nReturn: {borrower[4]}")
        found_count += 1

if found_count == 0:
    print("No matching books found.")

print("\n--- Final Tuple Borrowers List ---")
print(*borrowers, sep="\n")