# IMPORTS
from models import User
from database import insert_user, username_already_exists, user_pass_exists
users = [] # Empty list to hold users

def register_user(username, email, password, address):
    success_flag = False # Initialize success flag to False

    if username_already_exists(username):
        print("Error: Username already exists. Please choose a different username")
    # Check if the user input is empty
    elif len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0 or len(address.strip()) == 0:
        print("Error: certain input fields were left empty!")
    else:
        insert_user(username, email, password, address)
        print("User registered successfully!\n")
        success_flag = True
    return success_flag


def login_user(username, password):
    user = user_pass_exists(username, password)
    if user:
        return user
    else:
        return None

#def logout_user():