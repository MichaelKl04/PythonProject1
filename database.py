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


def insert_user(username, password, email, address): 

    # SQL query to insert a new user into the USERS table
    sql = "INSERT INTO USERS (user_username, user_password, user_email, user_address) VALUES (%s, %s, %s, %s)"
    
    # Define the values to be inserted into the query
    val = (username, password, email, address)

    # Execute hte SQL query with the provided values
    cursor.execute(sql, val)

    # Commit the transaction to the database
    conn.commit()



def insert_pet(Pname, Pbreed ,Panimal_type, Page, Ptemperament, Pgender, Pdate_broughtTo_Shelter, Plocation, Pstatus, Pimg):
    # SQL query to insert a new pet into the PETS table
    sql = "INSERT INTO PETS (pet_name, pet_breed, pet_type, pet_age, pet_temperament, pet_gender, pet_date_broughtTo_shelter, pet_location, pet_status, pet_img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Define the values to be inserted into the query
    pet = (Pname, Pbreed, Panimal_type, Page, Ptemperament, Pgender, Pdate_broughtTo_Shelter, Plocation, Pstatus, Pimg)

    # Execute the SQL query with the provided values
    cursor.execute(sql, pet)

    # Commit the transaction to the database
    conn.commit()

    


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
    # SQL query to select all from pets
    sql = "SELECT * FROM PETS"
    # Execute the SQL query to retrieve all pet records
    cursor.execute(sql)
    # Fetch all the pet records from the database
    pet_records = cursor.fetchall()

    # Initialize an empty list to store pet objects
    pets = []

    # Iterate over each pet record retrieved from teh database
    for record in pet_records:
        # Create a Pet Object from the record and append it to the pets list
        pet = Pet(id=record[0], 
                  name=record[1], 
                  breed=record[2], 
                  animal_type=record[3], 
                  age=record[4], 
                  temperament=record[5], 
                  gender=record[6], 
                  date_broughtTo_shelter=record[7], 
                  location=record[8],
                  status=record[9], 
                  pet_img=record[10])
        pets.append(pet)
    # Return the list of pet objects
    return pets

def export_app_records(adopted_pet, adopting_user, user_name, user_lname, adoption_date, user_phone, user_address):
    try:
        # SQL query to insert application records into the APPLICATION_RECORDS table
        sql = "INSERT INTO APPLICATION_RECORDS (adopted_pet, adopting_user, user_name, user_lname, adoption_date, user_phone, user_address) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        # Define the values to be inserted into the query
        values = (adopted_pet, adopting_user, user_name, user_lname, adoption_date, user_phone, user_address)
        
        # Execute the SQL query with the provided values
        cursor.execute(sql, values)
        
        # Commit the transaction to the database
        conn.commit()
        
        print("Application records exported successfully!")
    except mysql.connector.Error as error:
        print("Failed to export application records:", error)




# Close the cursor and connection when done
def close_connection():
    cursor.close()
    conn.close()
