
users = { "admin": "Admin","shop": "Shopkeeper","C101": "Customer","g21": "Guest"}

access = {"Admin": ["view", "add", "update", "delete"],"Shopkeeper": ["view", "add"],"Customer": ["view"],"Guest": []}

name = input("Enter your username: ")
choice = input("Enter required action: ")

if name not in users:
    print("Invalid username")
else:
    user_role = users[name]

    if choice in access[user_role]:
        print("Permission Allowed")
        print("Username:", name)
        print("Role:", user_role)
        print("Action:", choice)
    else:
        print("Permission Not Allowed")
        print(user_role, "cannot perform", choice)
