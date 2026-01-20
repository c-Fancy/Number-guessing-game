import random
import math

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

x = random.randint(lower, upper)

difficulty = input("Choose difficulty (easy/medium/hard): ").lower() 
if difficulty == "easy": multiplier = 1.5 
elif difficulty == "medium": multiplier = 1.0 
else: multiplier = 0.7 
total_chances = math.ceil(math.log(upper - lower + 1, 2) * multiplier)

print(f"\n\tYou've only {total_chances} chances to guess the "
           "integer!\n\n")

Count = 0
Flag = False

while Count < total_chances:
    Count += 1
    guess = int(input("Your guess number is: "))

    if x == guess:
        print(f"Congratulations! You did it in {Count} attempts.")
        Flag = True
        break

    elif x > guess:
        print("Sorry, your guess is too low.")

    elif x < guess:
        print("Sorry, your guess is too high.")

if not Flag:
    print(f"\nThe number is {x}")
    print("\nBetter luck next time!")