# name, card_number, book_issued_name, issue_date, return_date
borrowers = []
name =[
    'Anas Ahmed',
    'Bilal Khan',
    'Catherine Lee',
    'David Smith',
    'Eva Johnson'
]
card_number = [
    'C12345',
    'C23456',
    'C34567',
    'C45678',
    'C56789'
]
book_issued_name = [
    'The Great Gatsby',
    '1984',
    'To Kill a Mockingbird',
    'Pride and Prejudice',
    'On War'
]
issue_date = [
    '01-09-2023',
    '05-09-2023',
    '10-09-2023',
    '15-09-2023',
    '20-09-2023'
]
return_date = [
    '01-10-2023',
    '05-10-2023',
    '10-10-2023',
    '15-10-2023',
    '20-10-2023'
]

borrowers = [
    [name[0], card_number[0], book_issued_name[0], issue_date[0], return_date[0]], 
    [name[1], card_number[1], book_issued_name[1], issue_date[1], return_date[1]],
    [name[2], card_number[2], book_issued_name[2], issue_date[2], return_date[2]],
    [name[3], card_number[3], book_issued_name[3], issue_date[3], return_date[3]],
    [name[4], card_number[4], book_issued_name[4], issue_date[4], return_date[4]],
]

to_search = "pride "

if(to_search.lower().strip() in borrowers):
    print("Found")
else:
    print("Not Found")

borrowers[0][2] = "The Great Gatsby - Special Edition"
borrowers[2][0] = "Fatima"

# print(*borrowers, sep="\n")