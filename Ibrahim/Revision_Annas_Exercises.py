#10 letter word limit
book_title = input("Enter any forms of text:")
print(book_title[0:10].replace(" ", "_")) 

#palindrome
palindrome = input("Write a palindrome:")
print(palindrome[::-1].lower()) 

#Search engine inside lists Inworking

list_storage = ["Iran", "Afganistan", "Palistine", "Russia", "China"]
list_input = ["injail"]

if input("Input Text:").lower().strip() in list_storage:
    print("Yes")
else:
    print("No")