from collections import namedtuple

# Data lists remain the same
names = ['Anas Ahmed', 'Bilal Khan', 'Catherine Lee', 'David Smith', 'Eva Johnson']
card_numbers = ['C12345', 'C23456', 'C34567', 'C45678', 'C56789']
book_issued_names = ['The Great Gatsby', '1984', 'To Kill a Mockingbird', 'Pride and Prejudice', 'On War']
issue_dates = ['01-09-2023', '05-09-2023', '10-09-2023', '15-09-2023', '20-09-2023']
return_dates = ['01-10-2023', '05-10-2023', '10-10-2023', '15-10-2023', '20-10-2023']

# Define the structure of our records
# This acts like a lightweight class with specific field names
BorrowerRecord = namedtuple('BorrowerRecord', ['name', 'card_number', 'book_issued_name', 'issue_date', 'return_date'])

# Data lists remain the same as the first example...

borrowers_nt = [] # Use a new list name for clarity

# ... population logic remains similar, creating BorrowerRecord objects instead of raw tuples
if(len(names) == len(card_numbers) == len(book_issued_names) == len(issue_dates) == len(return_dates)):
    print("All lists are of equal length. Proceeding to create borrower records.")
    number_of_borrowers = len(names) # Get the length of any list since they are all equal

    for i in range(number_of_borrowers):
        borrower_record = BorrowerRecord(
            names[i],
            card_numbers[i],
            book_issued_names[i],
            issue_dates[i],
            return_dates[i]
        )
        borrowers_nt.append(borrower_record)

print("\n--- NamedTuple Records Created ---")
print(*borrowers_nt, sep="\n")


# ---------------------------------------------------
# ADD Functionality (NamedTuple)
# ---------------------------------------------------
def add_borrower_nt(name, card_num, book_name, issue_d, return_d):
    # Use field names for creation
    new_record = BorrowerRecord(name, card_num, book_name, issue_d, return_d)
    borrowers_nt.append(new_record)
    print(f"\nAdded new namedtuple borrower: {name}")

add_borrower_nt('Frank Adams (NT)', 'C67891', 'Dune (NT)', '25-09-2023', '25-10-2023')

# ---------------------------------------------------
# DELETE Functionality (NamedTuple)
# ---------------------------------------------------
def delete_borrower_by_card_nt(card_number_to_delete):
    global borrowers_nt
    # Use the field name for comparison
    borrowers_nt = [record for record in borrowers_nt if record.card_number != card_number_to_delete]
    print(f"\nDeleted namedtuple borrower with card number: {card_number_to_delete}")

delete_borrower_by_card_nt('C12345') # Deletes Anas Ahmed

# ---------------------------------------------------
# UPDATE Functionality (NamedTuple)
# ---------------------------------------------------
def update_book_name_nt(card_number_to_find, new_book_name):
    for i, record in enumerate(borrowers_nt):
        # Use field names for finding the record
        if record.card_number == card_number_to_find:
            # Namedtuples have a special helper method `_replace` to create a new instance
            # with specified fields updated, keeping the immutability pattern clean.
            updated_record = record._replace(book_issued_name=new_book_name)
            borrowers_nt[i] = updated_record
            print(f"\nUpdated book for {record.name} to '{new_book_name}' using namedtuple._replace()")
            return
    print(f"\nCard number {card_number_to_find} not found for namedtuple update.")

update_book_name_nt('C23456', 'The Hitchhiker\'s Guide to the Galaxy (NT)')


# ---------------------------------------------------
# SEARCH Functionality (NamedTuple)
# ---------------------------------------------------
to_search = "the "
print(f"\n--- Searching namedtuples for books containing '{to_search.strip()}' ---")

found_count_nt = 0
for borrower in borrowers_nt:
    # Use the named field access: record.book_issued_name
    if to_search.lower().strip() in borrower.book_issued_name.lower():
        print("Found")
        print("_" * 20)
        print(f"Name: {borrower.name}\nCard: {borrower.card_number}\nBook: {borrower.book_issued_name}")
        found_count_nt += 1

if found_count_nt == 0:
    print("No matching books found in namedtuple list.")

print("\n--- Final NamedTuple Borrowers List ---")
print(*borrowers_nt, sep="\n")