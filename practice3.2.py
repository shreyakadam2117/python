age = int(input("Enter your age: "))
income = float(input("Enter your annual family income: ₹"))

if age < 25 and income < 300000:
    print("Congratulations! You are eligible for the scholarship.")
else:
    print("Sorry! You are not eligible for the scholarship.")