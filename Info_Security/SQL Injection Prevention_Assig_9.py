
import sqlite3
import re

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL
)
""")

cursor.executemany(
    "INSERT INTO users (username) VALUES (?)",
    [("admin",), ("faculty",), ("student",)]
)

username = input("Enter username: ")

if not re.fullmatch(r"[A-Za-z0-9_]{1,20}", username):
    print("Invalid username format.")
else:
    cursor.execute(
        "SELECT username FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()

    if result:
        print("User found:", result[0])
    else:
        print("User not found.")

connection.close()
