
name = input("Enter your name: ")

for i in range(3):
    psw = input("Enter your password: ")

    if name == "devenz" and psw == "devz@123":
        print("Confidentiality: User Verified")

        value = input("Enter a value: ")

        if value == "5000":
            print("Integrity: Value is unchanged")
        else:
            print("Integrity: Value is changed")

        print("Availability: System is ready")
        break

    else:
        print("Invalid username or password")

else:
    print("Account Locked")
    print("Availability: Access denied")
