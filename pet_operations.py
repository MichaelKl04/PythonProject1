import os #OS Module to access system-specific functionality

# FUNCTION
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear') # Use cls on windows and clear on other platforms


def browse_available_pets(pets): # Function to browse through available pets
    page_size = 5
    current_page = 1
    total_pages = (len(pets) + page_size - 1) // page_size
    while True:
        # Display pets for the current page
        print("Available pets")
        start_index = (current_page - 1) * page_size # Starting index for the current page
        end_index = min(start_index + page_size, len(pets)) # Ending index for the current page
        # Display all the pets
        for i in range(start_index, end_index):
            print(f"{i + 1}. {pets[i].id}, {pets[i].name}, {pets[i].breed}, {pets[i].location}")
        
        #Display pagination information
        print(f"Page {current_page} of {total_pages}")
        if current_page > 1:
            print("Previous: P")
        if current_page < total_pages:
            print("Next: N")
        # Get user input
        choice = input("Enter pet ID to view details, or (N)ext/(P)revious/(Q)uit: ").strip().lower()
        # Handle user choices
        if choice == 'q':
            break # Break out of the loop to quit
        elif choice == 'n' and current_page < total_pages:
            current_page += 1 # Move to next page if possible
            clear_screen()
        elif choice == 'p' and current_page > 1:
            current_page -= 1 # Move to previous page if possible
            clear_screen()
        elif choice.isdigit():
            petId = int(choice)
            found = False

            for pet in pets:
                if pet.id == petId:
                    found = True
                    clear_screen()
                    view_pet_details(pets, petId)
            if not found:
                print("Error: Pet with specified ID does not exist.")
                input("Press Enter to continue...")
                clear_screen()
            
        else:
            print("Error: Invalid input")
            input("Press Enter to continue...")
            clear_screen()


        
def view_pet_details(pets, pet_id): # Function to view details of a specifc pet, ALSO where use can decide to adopt pet
    for pet in pets:
        if pet.id == pet_id:
            print(f"Now viewing {pet.name}'s Profile [{pet.id}]")
            print(f"{pet.name} is a {pet.age} year old {pet.breed} ({pet.animal_type}).")
            print(f"{pet.name} is very {pet.temperament}. {pet.name} was brought to us on ")
            print(f"{pet.date_broughtTo_shelter}, and currently resides at {pet.location}!")
            print(f"Adoption Status: {pet.status}\n")

            choice = input(f"Are you intrested in adopting {pet.name} (Y)es/(N)o? Or (Q)uit to exit: ").strip().lower()
            if choice == 'q':
                clear_screen()
                break




#def adopt_pet(user, pet_id) # Function to handle the adoption of a pet