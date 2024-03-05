# IMPORTS
import mysql.connector

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

    #Define the SQL quer to insert a new user into the USERS table
    sql = "INSERT INTO USERS (user_username, user_password, user_email, user_address) VALUES (%s, %s, %s, %s)"
    
    # Define the values to be inserted into the query
    val = (username, password, email, address)

    # Execute hte SQL query with the provided values
    cursor.execute(sql, val)

    # Commit the transaction to the database
    conn.commit()

# Close the cursor and connection when done
def close_connection():
    cursor.close()
    conn.close()
