import sqlite3 as sql
import requests as req

# Connect to the database
con = sql.connect("test.sqlite3")

# Create a cursor object
cur = con.cursor()

# Try to create the table, if it doesn't exist already
try:
    cur.execute("CREATE TABLE users(username, uuid)")
    print("Table created")
except:
    print("Table Exists, continuing")

# ---- RETURN A USER AND/OR UUID ---- #
def User_only(Username):
    SQL_Command = "SELECT * FROM users WHERE username='%s'" % str(Username)
    print(SQL_Command)
    res = cur.execute(SQL_Command)
    return res.fetchall()

Username = str(input("What is the username? "))
print(User_only(Username))
