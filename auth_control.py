# IMPORTS
from models import User
from database import insert_user
users = [] # Empty list to test Register and Login

def register_user(username, email, password, address):
    # Infinite loop incase user fails registration
    while True:
        #Check if the username already exists
        for user in users:
            if user.username == username:
                print("Error: Username already exists. Please choose a different username")
                return None
        else:
            new_user = User(username, password, email, address)
            # add the user to the list
            users.append(new_user)
            insert_user(username, password, email, address)
            print("User registered successfully!\n")
            return new_user



def login_user(username, password):
    while True:
        for user in users:
            if user.username == username:
                if user.password == password:
                    print(f"User {user.username} has logged in successfully!")
                    return user
                else:
                    print("Error: Invalid password was entered")
                    break
            else:
                print("Error: Invalid username was entered")
                break
        return None

def view_registered_users():
    for user in users:
        print(f"Username: {user.username}, Email: {user.email}, Address: {user.address}")

#def logout_user():