import random

top_Range = input("Care to guess a random number?: ")
if(top_Range.isdigit()):
    top_Range = int(top_Range)

    if(top_Range<=0):
        print("Please type a type a number bigger than 0")
        quit()
else:
    print("Type a number")
    quit()

random_number = random.randrange(0,top_Range)
while True:
    user_guess = input("Care to guess a random number?: ")
    if (user_guess.isdigit()):
        user_guess = int(top_Range)

        if (user_guess <= 0):
            print("Please type a type a number bigger than 0")
            quit()
    else:
        print("Type a number")
        continue
        quit()

print(random_number)
