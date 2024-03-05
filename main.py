# IMPORTS
from auth_control import register_user, login_user, view_registered_users, users
import os #OS Module to access system-specific functionality

# VARIABLES
username, password = "\0","\0"
welcome_shown = False

# FUNCTION
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear') # Use cls on windows and clear on other platforms

# MAIN
while True:
    clear_screen()
    if not welcome_shown:
        welcome_shown = True
        print("Welcome to the Adoption Centre\n")
    print("Would you like to:\n1.Register\n2.Login\n3.Exit\n4.View Users")
    menuInput = input("option: ")

    if menuInput == "1":
        while True:
            # Clear the screen
            clear_screen()
            # User enters their information
            username = input("Enter desired username: ")
            password = input("Enter desired password: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")

            # Pass users info to register function
            new_user = register_user(username, email, password, address)

            if new_user is not None: # If User registration was successful
                user_register_success = users[-1] # Get the last user in the list
                print(user_register_success)
                input("Press Enter to continue...")
                clear_screen()
                
                break # Back to main menu

            else: # User registration was not successful
                cancel_option = input("Login failed. Press Enter to try again, or enter 'Q' to cancel: ").strip().lower() # Allow user to retry or cancel
                if cancel_option == 'q': # If option is equal to q then break out the register_user method
                    break # Back to main menu
                
    elif menuInput == "2":
        while True:
            # Clear the screen
            clear_screen()

            # User input for login-in
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            logged_user = login_user(username, password)

            # if logged_user result is not equal to "None" -- Successful login
            if logged_user is not None:
                input("Press Enter to continue...")
                break
            else: # Unsuccessful login
                cancel_option = input("Login failed. Press Enter to try again, or enter 'Q' to cancel: ").strip().lower() # Allow user to retry or cancel
                if cancel_option == 'q': # If option is equal to q then break out the logged_user method
                    break # Back to main menu
    elif menuInput == "3":
        # Clear the screen
        clear_screen()
        print("Exiting program.")
        break
    elif menuInput == "4": # Temporary to see the list of registered users
        # If the amount of users is 0
        if len(users) == 0:
            print("No users registered.")
        else:
            print("Registered users:")
            view_registered_users()
        input("Press Enter to continue...")
    # If user inputs an incorrect option
    else:
        print("Error: Incorrect Option, try again.")
        input("Press Enter to continue...")




