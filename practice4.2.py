status = input("Enter atmospheric status: ").lower()

if status == "hot":
    print("Turn on AC")
elif status == "cold":
    print("Activate heater")
elif status == "normal":
    print("Idle")
else:
    print("Unknown atmospheric status")