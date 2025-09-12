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

'''
# ---- ADD A USER TO THE DATABASE ---- #
# Get the UUID of a specified user
username = str(input("What is the username? ")) # Get the username
get_url = "https://api.mojang.com/users/profiles/minecraft/" + username  # Create a url for getting the UUID
api_response = req.get(get_url) # Make the request and get the response

# Process the JSON, and handle any unexpected errors
if api_response.status_code == 200:
    json_response = api_response.json()
    UserID = json_response.get("id")
else:
    print("Try again")

# Define data set to be added
user_info = [
    (username, UserID),
]

# Add the data and commit the changes to the file
cur.executemany("INSERT INTO users VALUES(?, ?)", user_info)
con.commit()
'''