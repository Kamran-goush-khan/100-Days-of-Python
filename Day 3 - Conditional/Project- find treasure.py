print("Welcome to the Treasure Hunt!!")
path = input("Which direction will you choose? Type 'left' or 'right'")

if path == "Right" or path == "right" :
    print("Instead of treasure you have found the Dead End.\nGame Over")
else :
    is_swim = input("Do you want to do some exercise? Type 'swim' or 'wait' ")

    if is_swim == "swim" or is_swim == "Swim" :
        print("Instead of finding the treasure you have found some crocodile and snake in the water. Enjoy your death exercise\nGame Over")
    else :
        door = input("Which door you want to open? 'Red', 'Green' or 'Gray' ")

        if door == "red" or door == "Red" :
            print("You have chosen the color of blood now bath in it.\nGame Over")
        elif door == "Green" or door == "green" :
            print("You think Green is safe but in my opinion it is a straight path to the heaven.\nGame Over")
        else :
            print("You made every decision correct and here is your treasure of ₹100😂😂")