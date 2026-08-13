print("*****************DAILY CALORIE TRACKER*************")

total_calorie = 0

while True:
    food = input("Enter a food name(or type 'done' to finish):")

    if food.lower() == "done":
        break
    calories=float(input("Enter calories:"))

    total_calorie +=calories

    print(food,"Added Successfuly!")
    print(" current total calories:",total_calorie)
    print("\n=====================================\n")
    print("total calories today:",total_calorie)
    print("\n======================================\n")
    print("Thank you for using calorie tracker")