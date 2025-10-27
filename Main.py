# WELCOME_MESSAGE = "Welcome to Learning python on VsCode"
# #participant1 for the LibraryManagementSystem
# participant_1 = input("Enter participiant1 : ")
# # #participant2 for the LibraryManagementSystem
# participant_2 = input("Enter participiant2: ")


# #Welcome_message = "Welcome to Learning python on Vs "
# ##participant_2 = input("Enter your name: ")

# # paricipiant_3, participiant_4 = "Asad" , "Fawad"
# # #legal variables

# # print(WELCOME_MESSAGE + " " + participant_1 + " and " + participant_2)
# # print(WELCOME_MESSAGE , participant_1  , participant_2, paricipiant_3 , "and", participiant_4)



# print("Asad" == "Asad")
# #type casting
# print("Asad " + str(3))
# print(WELCOME_MESSAGE + participant_1 + " and " + participant_2)

# #Multiline string
# MESSAGE = """This is a simple program to demonstrate input and output in Python.  
# You will be asked to enter your names."""

# participant_1 = "Ibrahim"
# participant_2 = "Anas"

# #lists
# list_of_participants = [participant_1, participant_2, 1 , 23.4, True]

# list_of_participants = [[participant_1, participant_2 ] ,[44.5 , 52.4] ]

# # print(list_of_participants)

# # for index in range(5):
# #     print("$" * int(index + 1))
# # print(len(participant_1))
# # print(participant_1[2:len(participant_1)])

# # if(participant_1[2:len(participant_1)] == "brahim"): #checking substring
# #     print("Yes")
# # else:
# #     print("No")

# # if(participant_1[2:3] in "brahim"): #in string function
# #     print("Yes")
# # else:
# #     print("No")

# # print("-".join(participant_1)) #joining string with separator
# # print(participant_1.swapcase()) #capitalizing first letter of string
# # print("-".join(reversed(participant_1)))


'''
LISTS
'''
fruits = ["apple", "banana", "cherry", "date"]

more_fruits = ["elderberry", "fig", "grape"]

# fruits += more_fruits
fruits = fruits + more_fruits
# fruits[2] = "citrus"
fruits.insert(2, "citrus")

fruits.sort()
fruits.reverse()
print(*fruits, sep=f"\n")