password="shreya"

while True:
     password = input("Enter the password: ")
     if password ==password:
        print(" Access Granted!")
        break
     else:
        print(" Wrong password, try again...")

print("*************************WITHOUT BREAK********************************")

correct_password = "shreya"

while True:
    entered_password = input("Enter the password: ")
    if entered_password == correct_password:
        print("Access Granted!")
        
        exit()
    else:
        print("Wrong password, try again...")
