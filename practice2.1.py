# Student Scorecard

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n----- FINAL SCORECARD -----")
print("Subject 1:", mark1)
print("Subject 2:", mark2)
print("Subject 3:", mark3)
print("Total    :", total)
print("Average  :", round(average, 2))