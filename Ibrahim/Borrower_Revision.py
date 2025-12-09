#Create 5 lists including Names, Card Numbers, Book Issued Names, Issue Dates, Return Dates
names = [
    'Mao Zedong',
    'Adolf Hitler',
    'Joseph Stalin',
    'Osama Bin Laden',
    'Gengius Khan'
]

card_numbers = [
    'C67890',
    'C78901',
    'C89012',
    'C90123',
    'C01234'
]

book_names = [
    'The Art of War',
    'Mein Kampf',
    'The Communist Manifesto',
    'The 9/11 Commission Report',
    'The Sons of Genghis Khan'
]

issue_dates = [
    '02-09-1923',
    '01-09-1939',
    '21-12-1945',
    '11-09-2001',
    '01-01-1206'
]

return_dates = [
    '02-10-1923',
    '01-10-1939',
    '21-01-1946',
    '11-10-2001',
    '01-02-1206'
]

arranged_list = []


#Make the list len equal to each other
if len(names) == len(card_numbers) == len(book_names) == len(issue_dates) == len(return_dates):
    print("The length of the 5 lists are same")
    length_of_lists = len(names)

    for i in range(length_of_lists) :

      format_list = [

           names[i],
           card_numbers[i],
           book_names[i],
           issue_dates[i],
           return_dates[i]
     ]

      arranged_list.append(format_list) 

print(arranged_list[3])