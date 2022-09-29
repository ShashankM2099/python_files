# number_list  = [10,20,35,45,60,99]
#
# ## displaying numbers that are divisible are 5
#
# for num in number_list :
#     if num%5==0:
#         print("The Words", num)
#
# str = "Shashank did this. Shashank did that. Shashank done that."
# count = str.count("Shashank")
# print(count)
#
# # Printing strings at an even index number
# newString = "This is a string. Printing at even."
# size = len(newString)
# newString.strip(" ")
# for r in range(0,size-1,2):
#     print("Index",r,"and", newString[r])

## See if the first and last of the num list are the same
#
# def first_last_sameList(list):
#     first = list[0]
#     last = list[-1]
#
#     return first==last
#
# num_list = [10,45,1231,1234343,10]
# print("List: ", first_last_sameList(num_list))
import random

computer_choice = random.choice(["Rock", "Paper", "Scissors"])
userChoice = input("What is your choice \n1.Rock \n2.Paper \n3.Scissors \n")

if computer_choice == userChoice:
    print("TIE: Computer Chose", computer_choice)
elif userChoice == "Rock" and computer_choice == "Scissors":
    print("You win :O and the computer chose", computer_choice)
elif userChoice == "Paper" and computer_choice == "Rock":
    print("You win the computer chose", computer_choice)
elif userChoice == "Scissors" and computer_choice == "Paper":
    print("You win the computer chose", computer_choice)

else:
    print(f"Computer chose {computer_choice}, so Computer wins")

gameList = {"Red Dead Redemption": "RockStar",
            "Marvel Spider-Man": "Insomniac",
            "Marvel Snap": "Second Dinner",
            "DBZ Kakarot": "Bandai Namco"}
print("WE got the current Games")
for key,value in gameList:
    print(key, "is made by", value, sep='')

