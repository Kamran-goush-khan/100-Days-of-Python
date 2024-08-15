import random

# a = random.randint(0, 10)  # Generate random integer in the given range
# print(a)
# a = random.random() * 10   # Generate random number in the range 0 to 1(exclusive)
# print(a)
# print(random.uniform(0, 5))

# Program for generating Head and Tail in random way.
number = round(random.random() * 10)
if number < 5 :
    print("Head")
else :
    print("Tail")
