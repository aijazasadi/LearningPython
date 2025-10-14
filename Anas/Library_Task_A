"""
Why_nations_go_to_war = "name: Why nations go to war, author: John G. Stoessinger, genre: Political Science, publisher: Cengage Learning, language: English"
The_Art_of_War = "name: The Art of War, author: Sun Tzu, genre: Military Strategy, publisher: Oxford University Press, language: English"
The_Prince = "name: The Prince, author: Niccolò Machiavelli, genre: Political Philosophy, publisher: Penguin Classics, language: English"
On_War = "name: On War, author: Carl von Clausewitz, genre: Military Theory, publisher: Princeton University Press, language: English"
The_33_Strategies_of_War = "name: The 33 Strategies of War, author: Robert Greene, genre: Self-Help, publisher: Profile Books, language: English"
The_Campaigns_of_Alexander = "name: The Campaigns of Alexander, author : Arrian, genre: History, publisher: Penguin Classics, language: English"





Books = [Why_nations_go_to_war, The_Art_of_War, The_Prince, On_War, The_33_Strategies_of_War, The_Campaigns_of_Alexander]


book_name = input("Enter book name: ")
#dd-mm-yyyy
book_issue_date = input("Enter book issue date: dd,mm,yyyy ")
#dd-mm-yyyy
book_return_date = input("Enter book return date: dd-mm-yyyy")


print('Why nations go to war', 'The_Art_of_War', 'The_Prince, On_War', 'The_33_Strategies_of_War', 'The_Campaigns_of_Alexander')
WHICH_BOOK = input("which book you want to issue: ")

if WHICH_BOOK == "Why nations go to war":
    print(Why_nations_go_to_war)
elif WHICH_BOOK == "The_Art_of_War":
    print(The_Art_of_War)
elif WHICH_BOOK == "The_Prince":
    print(The_Prince)
elif WHICH_BOOK == "On_War":
    print(On_War)
elif WHICH_BOOK == "The_33_Strategies_of_War":
    print(The_33_Strategies_of_War)
elif WHICH_BOOK == "The_Campaigns_of_Alexander":
    print(The_Campaigns_of_Alexander)
else:
    print("Book not available")

print("You will issue this book by", book_issue_date, "You will return this book by", book_return_date)
"""

book_names = [
    'Why_nations_go_to_war', 
    'The_Art_of_War',
    'The_Prince', 
    'On_War', 
    'The_33_Strategies_of_War' 
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


input_book_index = int(input("Enter book index (0-4): "))


if(input_book_index >=0 or input_book_index < len(book_names)): 
    print("You have selected book: ", book_names[input_book_index])
    print("Book Author: ", book_authors[input_book_index])
    print("Book Issue Date: ", book_issue_dates[input_book_index])
    print("Book Return Date: ", book_return_dates[input_book_index])
else:
    print("Invalid book index")