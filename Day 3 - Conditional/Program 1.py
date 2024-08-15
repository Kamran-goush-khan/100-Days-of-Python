print("Welcome to the RollerCoaster!")
height = int(input("Please Enter Your Height "))
amount = 0


if height > 120 :
    print("You can ride the rollercoaster")
    age = int(input("Enter your age ? "))
    if age >= 45 and age <= 55 :
        print("No charges for the ride!!")
    elif age <= 12 :
        print("Child ticket price is ₹20")
        amount = 20
    elif age <= 18 :
        print("Youth ticket price is ₹25")
        amount = 25
    else :
        print("Adult ticket price is ₹35")
        amount = 35
    want_photo = input("Do you want to take photo? Type 'y' for yes and 'n' for no. ")
    if want_photo == "y" :
        amount += 3
    print(f"You have to pay ₹{amount}")
else :
    print("You need to grow taller you can't ride right now.")