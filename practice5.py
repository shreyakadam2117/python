n = int(input("Enter the number of rows: "))

for i in range(2, n + 2):
    for j in range(2, i + 2):
        print(j, end=" ")
    print()