print("**********STAR PATTERN************")

rows=5
for i in range (rows):
    for j in range (rows -i-1):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

print("*****************NUMBER PATTERN************")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("Invoice + Receipt Pattern***********")


rows = 5
print("INVOICE".center(20, "*"))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("RECEIPT".center(20, "*"))

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()