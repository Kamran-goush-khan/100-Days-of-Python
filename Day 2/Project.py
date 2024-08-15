# Tip calculator

print("Welcome to the Tip Calculator😀")
bill = float(input("What was the total bill? ₹"))
tip = float(input("How much tip would you like to give 10, 12 or 15? ₹"))
people = float(input("How many people to split the bill? "))
total_amount = bill * (1 + (tip / 100))
result = total_amount / people
print(f"Each person have to pay ₹{round(result, 2)}")