import random

# range of the values of a dice
min_val = 1
max_val = 6

x = int(input("Enter your favourite number="))
print("Rolling the dice to see if it is your favourite number")
dice = "y"

while dice == "y":

    value = random.randint(min_val, max_val)
    print("Dice value is =", value)
    if value == x:
        print("Great!!!!!!!!.....You Got it CORRECT........Your Number and DICE generated is same")
        break
    else:
        print("SORRY!!!..Its different")
        dice = input("Do you want to continue=")

print("The Game is COMPLETE")
input("Press any Key to Exit")
