print("************Consumer Transaction Tracker**********")

transactions = []
for i in range(5):
    amount = float(input(f"Enter transaction {i+1}: "))
    transactions.append(amount)

largest_transaction = max(transactions)

average_spend = sum(transactions) / len(transactions)

print("\n--- Transaction Summary ---")
print(f"Transactions: {transactions}")
print(f"Largest Transaction: ₹{largest_transaction}")
print(f"Average Spend: ₹{average_spend:.2f}")


print("**************Student Score Filter Script**********")
grades = []
n = int(input("Enter number of grades: "))
for i in range(n):
    grade = int(input(f"Enter grade {i+1}: "))
    grades.append(grade)

print("\nOriginal Grades:", grades)

index = int(input("Enter the index position to update (0-based): "))

if 0 <= index < len(grades):
    new_grade = int(input("Enter the new grade: "))
    grades[index] = new_grade
    print("\n Grade updated successfully!")
else:
    print("\n Invalid index position!")

print("Corrected Grades:", grades)
