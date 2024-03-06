# IMPORTS
import mysql.connector
from models import Pet

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost", #Local
    user="root", # Check by running "select user();" inside MySQL
    password="", # Enter your own username
    database="PetAdoptionSystem" # Name of Database
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Function used inside auth_control.py --> register_user()
def insert_user(username, email, password, address): 

    # SQL query to insert a new user into the USERS table
    sql = "INSERT INTO USERS (user_username, user_password, user_email, user_address) VALUES (%s, %s, %s, %s)"
    
    # Define the values to be inserted into the query
    val = (username, password, email, address)

    # Execute hte SQL query with the provided values
    cursor.execute(sql, val)

    # Commit the transaction to the database
    conn.commit()

# Function used inside auth_control.py --> register_user()
def username_already_exists(username):
    # SQL query to check if the username exists
    sql = "SELECT * FROM USERS WHERE user_username = %s"
    # Execute the SQL query with the provided username
    cursor.execute(sql,(username,))
    # Fetch the result
    result = cursor.fetchone()
    # Return True if the result is not None, indicating the username exists
    return result is not None

def user_pass_exists(username, password):
    # SQL query to check if the username and password match
    sql = "SELECT * FROM USERS WHERE user_username = %s AND user_password = %s"
    # Execuute the SQL query with the provided username and password
    cursor.execute(sql, (username, password))
    # Fetch the first row from the result
    user = cursor.fetchone()

    if user:
        print(f"User {user[1]} has logged in successfully!")
        return user
    else:
        print("Error: Invalid username or password")
        return None
    
def import_pets():
    sql = "SELECT * FROM PETS"
    cursor.execute(sql)
    pet_records = cursor.fetchall()

    pets = []

    for record in pet_records:
        pet = Pet(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9])
        pets.append(pet)
    return pets

# Close the cursor and connection when done
def close_connection():
    cursor.close()
    conn.close()
