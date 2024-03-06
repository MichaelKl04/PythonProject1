# IMPORTS
from auth_control import register_user, login_user
from pet_operations import browse_available_pets, clear_screen
from database import import_pets

# VARIABLES
username, password = "\0","\0"
welcome_shown = False

# MAIN
while True:
    clear_screen()
    if not welcome_shown:
        welcome_shown = True
        print("Welcome to the Adoption Centre\n")
    print("Would you like to:\n1.Register\n2.Login\n3.Exit\n")
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
            registration = register_user(username, email, password, address)

            if registration: # If User registration was successful
                input("User registered successfully! Press Enter to continue...")
                break # Back to main menu

            else: # User registration was not successful
                cancel_option = input("Registration failed. Press Enter to try again, or enter 'Q' to cancel: ").strip().lower() # Allow user to retry or cancel
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
                clear_screen()
                break

            else: # Unsuccessful login
                cancel_option = input("Login failed. Press Enter to try again, or enter 'Q' to cancel: ").strip().lower() # Allow user to retry or cancel
                if cancel_option == 'q': # If option is equal to q then break out the logged_user method
                    break # Back to main menu
        if logged_user is not None:
            browse_available_pets(import_pets())
    elif menuInput == "3":
        # Clear the screen
        clear_screen()
        print("Exiting program.")
        break
    # If user inputs an incorrect option
    else:
        print("Error: Incorrect Option, try again.")
        input("Press Enter to continue...")




