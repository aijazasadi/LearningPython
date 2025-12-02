# name, card_number, book_issued_name, issue_date, return_dates
borrowers = []
names =[
    'Anas Ahmed',
    'Bilal Khan',
    'Catherine Lee',
    'David Smith',
    'Eva Johnson'
]
card_numbers = [
    'C12345',
    'C23456',
    'C34567',
    'C45678',
    'C56789'
]
book_issued_names = [
    'The Great Gatsby',
    '1984',
    'To Kill a Mockingbird',
    'Pride and Prejudice',
    'On War'
]
issue_dates = [
    '01-09-2023',
    '05-09-2023',
    '10-09-2023',
    '15-09-2023',
    '20-09-2023'
]
return_dates = [
    '01-10-2023',
    '05-10-2023',
    '10-10-2023',
    '15-10-2023',
    '20-10-2023'
]
# Creating borrower records manually
# borrowers = [
#     [names[0], card_numbers[0], book_issued_names[0], issue_dates[0], return_dates[0]], 
#     [names[1], card_numbers[1], book_issued_names[1], issue_dates[1], return_dates[1]],
#     [names[2], card_numbers[2], book_issued_names[2], issue_dates[2], return_dates[2]],
#     [names[3], card_numbers[3], book_issued_names[3], issue_dates[3], return_dates[3]],
#     [names[4], card_numbers[4], book_issued_names[4], issue_dates[4], return_dates[4]],
# ]
# Alternative way to create borrower records
if(len(names) == len(card_numbers) == len(book_issued_names) == len(issue_dates) == len(return_dates)):
    print("All lists are of equal length. Proceeding to create borrower records.")
    number_of_borrowers = len(names) # Get the length of any list since they are all equal

    for i in range(number_of_borrowers):
        borrower_record = [
            names[i],
            card_numbers[i],
            book_issued_names[i],
            issue_dates[i],
            return_dates[i]
        ]
        borrowers.append(borrower_record)

to_search = "de "

for borrower in borrowers:
    #you can define constants for indices to make it more readable
    if to_search.lower().strip() in borrower[2].lower(): # book_issued_name is at index 2
        print("Found")
        print("_" * 20)
        print(*borrower, sep="\n")
        break

# print(*borrowers, sep="\n")
