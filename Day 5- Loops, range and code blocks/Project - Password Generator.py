import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator")
nr_letters = int(input("How many letter do you want in your password? "))
nr_numbers = int(input("How many numbers do you want in your password? "))
nr_symbols = int(input("How many symbols do you want in your password? "))

#Easy Version
# password = ""
# for i in range(0, nr_letters) :
#     password += random.choice(letters)
#
# for i in range(0, nr_numbers) :
#     password += random.choice(numbers)
#
# for i in range(0, nr_symbols) :
#     password += random.choice(symbols)
#
# print(password)


#Hard Version

total_types = ["nr_letters", "nr_symbols", "nr_numbers"]
total_iteration = nr_symbols + nr_letters + nr_numbers
password = ""

for i in range(0, total_iteration) :

    if nr_letters == 0 and "nr_letters" in total_types:
        total_types.remove("nr_letters")
    if nr_numbers == 0 and "nr_numbers" in total_types:
        total_types.remove("nr_numbers")
    if nr_symbols == 0 and "nr_symbols" in total_types:
        total_types.remove("nr_symbols")

    chosen_type = random.choice(total_types)

    if chosen_type == "nr_letters" :
        password += random.choice(letters)
        nr_letters -= 1
    elif chosen_type == "nr_numbers" :
        password += random.choice(numbers)
        nr_numbers -= 1
    elif chosen_type == "nr_symbols" :
        password += random.choice(symbols)
        nr_symbols -= 1

print(password)

