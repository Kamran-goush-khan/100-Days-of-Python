def add(n1, n2):
    """this function take two number and return their sum"""
    return n1 + n2


def subtract(n1, n2):
    """This function take two number and give their difference"""
    return n1 - n2


def multiply(n1, n2):
    """This function take two number and return their product"""
    return n1 * n2


def divide(n1, n2):
    """This function take two number and return their division"""
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

user_opinion = "r"
result = 0
number = 0

while True:

    if user_opinion == "r":
        number = int(input("Enter the first number. "))
    elif user_opinion == "y":
        number = result

    first_number = number

    for operator in operation:
        print(operator)

    opr = input("Please select the operation you want to perform. ")

    second_number = int(input("Please Enter next number. "))

    fun = operation[opr]
    result = fun(first_number, second_number)
    print(f"{first_number} {opr} {second_number} = {result}")

    user_opinion = input(
        "Type 'y' for continue, 'r' to restart the calculation and 'e' to end the calculator.\n").lower()

    if user_opinion == "e" :
        break
    elif user_opinion != "r" and user_opinion != "y" :
        print(f"You have entered the wrong text '{user_opinion}'. Your last calculated result is {result}")
        break

