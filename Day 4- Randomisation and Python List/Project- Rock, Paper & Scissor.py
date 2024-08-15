import random

user_choice = int(input("What do you want to choose? Type 1 for 'rock', 2 for 'paper' and 3 for 'scissor' "))
computer_choice = random.randint(1, 3)

# code for when user choose rock
if user_choice == 1:
    if computer_choice == 1:
        print("You both like rock, so it,s a draw.")
    elif computer_choice == 2:
        print("Computer is worthy opponent, as it choose paper.\nComputer Win")
    else:
        print("Well computer is still computer and its choose scissor, but you have shown great skills😁.\nYou Win")

# code for when user choose paper
elif user_choice == 2:
    if computer_choice == 1:
        print("Well computer is still computer and its choose rock, but you have shown great skills😁.\nYou Win")
    elif computer_choice == 2:
        print("You both like paper, so it,s a draw.")
    else:
        print(
            "Computer is worthy opponent, as it choose scissor.\nComputer Win")

# code for when user choose scissor
elif user_choice == 3:
    if computer_choice == 1:
        print("Computer is worthy opponent, as it choose rock.\nComputer Win")
    elif computer_choice == 2:
        print("Well computer is still computer and its choose paper, but you have shown great skills😁.\nYou Win")
    else:
        print("You both like scissor, so it,s a draw.")

# when user have chosen something else
else:
    print("You have not selected the given option")
