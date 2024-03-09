import tkinter as tk
from tkinter import ttk
from database import insert_user, username_already_exists, user_pass_exists, import_pets, insert_pet, export_app_records

currentFrame = None
exisiting_users = {} # Keep track of exisiting users

class Menu:
  def __init__(self):
    self.window = window
    self.frame = tk.Frame()

    self.register_button = tk.Button(
      master=self.frame, 
      text="Register", 
      command=self.open_register, 
      width=25,
      bg="green",
      fg="yellow"
      )
    self.login_button = tk.Button(
      master=self.frame, 
      text="Login", 
      command=self.open_login, 
      width=25,
      bg="green",
      fg="yellow"
      )
    self.exit_button = tk.Button(
      master=self.frame,
      text="Exit",
      width=25,
      bg="green",
      fg="yellow",
      command=self.window_quit
      )

    self.register_button.pack(pady=5)
    self.login_button.pack(pady=5)
    self.exit_button.pack(pady=5)

    self.frame.pack()

  def open_register(self):
    register_page = Register()
    self.frame.destroy()

  def open_login(self):
    login_page = Login()
    self.frame.destroy()

  def window_quit(self):
    window.quit()
    #--------------------------------  

class Register:
  def __init__(self):
    self.frame = tk.Frame()

    self.registerLabel = tk.Label(master=self.frame, text="Register")
    self.userLabel = tk.Label(master=self.frame, text="Enter a Name")
    self.user = tk.Entry(master=self.frame, fg="white", bg="dimgrey", width=30)
    self.pwdLabel = tk.Label(master=self.frame, text="Enter a Password")
    self.pwd = tk.Entry(master=self.frame, fg="white", bg="dimgrey", width=30)
    self.addrLabel = tk.Label(master=self.frame, text="Enter your Address")
    self.addr = tk.Entry(master=self.frame, fg="white", bg="dimgrey", width=30)
    self.emailLabel = tk.Label(master=self.frame, text="enter your Email")
    self.email = tk.Entry(master=self.frame, fg="white", bg="dimgrey", width=30)
    self.err_msg = tk.Label(master=self.frame, fg="red")
    self.scs_msg = tk.Label(master=self.frame, fg="green") 
    self.registerButton = tk.Button(
      master=self.frame,
      text="Register",
      width=25,
      bg="green",
      fg="yellow",
      command=self.register_user
    )
    self.menuButton = tk.Button(
      master=self.frame, 
      text="Exit", 
      width=25,
      bg="green",
      fg="yellow",
      command=self.back_to_menu
      )

    self.err_msg.pack()
    self.scs_msg.pack()
    self.registerLabel.pack()
    self.userLabel.pack()
    self.user.pack()
    self.pwdLabel.pack()
    self.pwd.pack()
    self.addrLabel.pack()
    self.addr.pack()
    self.emailLabel.pack()
    self.email.pack()
    self.registerButton.pack(pady=5)
    self.menuButton.pack(pady=5)

    self.frame.pack()
    
  def register_user(self):
      username = self.user.get().strip()
      password = self.pwd.get().strip()
      address = self.addr.get().strip()
      email = self.email.get().strip()
      if len(username) == 0 or len(password) == 0 or len(address) == 0 or len(email) == 0: # Ensure user has filled out all fields
        self.err_msg.config(text="Error: Not all fields were entered.")
      else:
        self.scs_msg.config(text="") # Clear success message
        if username_already_exists(username):
          self.err_msg.config(text="Error: Username already exists.")
          self.scs_msg.config(text="") # Clear success message
        else:
          insert_user(username, password, email, address)
          self.scs_msg.config(text="Registration successful.")
          self.err_msg.config(text="") # Clear error message
          self.frame.after(1500, self.back_to_menu)

  def back_to_menu(self):
        menu_page = Menu()
        self.frame.destroy()

    
class Login:
  def __init__(self):
    self.frame = tk.Frame()

    self.userLabel = tk.Label(master=self.frame, text="User Name")
    self.user = tk.Entry(master=self.frame, fg="white", bg="gray", width=30)

    self.pwdLabel = tk.Label(master=self.frame, text="Password")
    self.pwd = tk.Entry(master=self.frame, show="*",fg="white", bg="gray", width=30)

    self.loginButton = tk.Button(
	  	master=self.frame,
	  	text="Login",
	  	width=25,
	  	bg="green",
	  	fg="yellow",
	  	command= lambda: self.log_in(currentFrame),
	  )
    self.menuButton = tk.Button(
      master=self.frame, 
      text="Exit", 
      width=25,
      bg="green",
      fg="yellow",
      command=self.back_to_menu
    )

    self.err_msg = tk.Label(master=self.frame, fg="red")
    self.scs_msg = tk.Label(master=self.frame, fg="green")

    self.userLabel.pack()
    self.user.pack()
    self.pwdLabel.pack()
    self.pwd.pack()
    self.loginButton.pack(pady=15)
    self.err_msg.pack()
    self.scs_msg.pack()
    self.menuButton.pack()

    self.frame.pack()

  def destroy_self(self):
    self.frame.destroy()

  def back_to_menu( self):
    menu_page = Menu()
    self.frame.destroy()

  def log_in(self, cf):
    username = self.user.get()
    password  = self.pwd.get()
    user = user_pass_exists(username, password)
    if user:
          self.err_msg.config(text="") # Clear error message
          self.scs_msg.config(text=f"Welcome {user[1]}!")
          self.frame.after(1000, self.login_complete)
    else:
      self.err_msg.config(text="Error: Invalid username or password.")

  def login_complete(self):
    logged_in = Admin_menu()
    self.destroy_self()

#--------------------------------  
      
class Admin_menu:
  def __init__(self):
    self.admin_menu = tk.Frame(window)

    self.animal_list = tk.Button(
      master=self.admin_menu,
      text="List of pets",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.display_pet_list(currentFrame)
    )

    self.add_pet = tk.Button(
      master=self.admin_menu,
      text="Add pet",
      width=25,
      bg="green",
      fg="yellow",
      
      command= lambda: self.display_add_pet(currentFrame)
    )

    self.remove_pet = tk.Button(
      master=self.admin_menu,
      text="Remove pet",
      width=25,
      bg="red",
      fg="yellow",
    )

    self.view_adoptions = tk.Button(
      master=self.admin_menu,
      text="View adoption applications",
      width=25,
      bg="red",
      fg="yellow",
    )

    self.logout = tk.Button(
      master=self.admin_menu,
      text="Logout",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.log_admin_out(currentFrame)
    )

    self.animal_list.pack()
    self.add_pet.pack()
    self.remove_pet.pack()
    self.view_adoptions.pack()
    self.logout.pack()

    self.admin_menu.pack()

  # functions for each menu
  
  def display_pet_list(self, cf):
    cf = Pet_list()
    self.admin_menu.destroy()

  def display_add_pet(self, cf):
    self.admin_menu.destroy()
    cf = Add_Pet()

  def log_admin_out(self, cf):
    cf = Login()
    self.admin_menu.destroy()

#--------------------------------  
    
class Pet_list:
    def __init__(self):
        self.pet_list = tk.Frame()
        self.pets = import_pets()

        self.display_pets()

        self.return_button = tk.Button(
            master=self.pet_list,
            text="Return",
            width=25,
            bg="green",
            fg="yellow",
            command=self.return_menu
        )

        self.return_button.pack(pady=5)
        self.pet_list.pack(pady=5)

    def display_pets(self):

        for pet in self.pets:
            pet_button = tk.Button(
                master=self.pet_list,
                width=60,
                anchor="w",
                text=f"Name: {pet.name}, Breed: {pet.breed}, Location: {pet.location}, Status: {pet.status}",
                command=lambda p=pet: self.show_pet_details(p)
            )
            pet_button.pack(pady=5)

    def show_pet_details(self, pet):
      details = Show_Details(self.pet_list, pet)
 
    def return_menu(self,):
      back = Admin_menu()
      self.pet_list.destroy()

#--------------------------------  

class Show_Details:
    def __init__(self, parent, pet):
        self.pet = pet
        self.parent = parent
        self.detail_frame = tk.Frame(self.parent)

        # labels for each attribute
        self.pet_id_label = tk.Label(self.detail_frame, text=f"ID: {pet.id}")
        self.pet_name_label = tk.Label(self.detail_frame, text=f"Name: {pet.name}")
        self.pet_breed_label = tk.Label(self.detail_frame, text=f"Breed: {pet.breed}")
        self.pet_type_label = tk.Label(self.detail_frame, text=f"Type: {pet.animal_type}")
        self.pet_age_label = tk.Label(self.detail_frame, text=f"Age: {pet.age}")
        self.pet_temperament_label = tk.Label(self.detail_frame, text=f"Temperament: {pet.temperament}")
        self.pet_gender_label = tk.Label(self.detail_frame, text=f"Gender: {pet.gender}")
        self.pet_date_broughtTo_shelter_label = tk.Label(self.detail_frame, text=f"Date Brought to Shelter: {pet.date_broughtTo_shelter}")
        self.pet_location_label = tk.Label(self.detail_frame, text=f"Location: {pet.location}")
        self.pet_status_label = tk.Label(self.detail_frame, text=f"Status: {pet.status}")
        self.pet_img_label = tk.Label(self.detail_frame, text=f"Image: {pet.img_url}")

        # Pack labels
        self.pet_id_label.pack()
        self.pet_name_label.pack()
        self.pet_breed_label.pack()
        self.pet_type_label.pack()
        self.pet_age_label.pack()
        self.pet_temperament_label.pack()
        self.pet_gender_label.pack()
        self.pet_date_broughtTo_shelter_label.pack()
        self.pet_location_label.pack()
        self.pet_status_label.pack()
        self.pet_img_label.pack()
        # Adopt Button
        self.apply_button = tk.Button(
           self.detail_frame, 
           text="Apply for Adoption", 
           bg="green",
           width=25,
           command=self.apply_for_adoption
           )
        self.apply_button.pack()
        # Return button
        self.return_button = tk.Button(
            self.detail_frame,
            text="Clear",
            width=25,
            bg="green",
            command=self.return_to_pet_list
        )
        self.return_button.pack()

        # Pack detail frame
        self.detail_frame.pack()

    def apply_for_adoption(self):
            self.detail_frame.destroy()
            app_page = Application(self.parent, self.pet)
       
    def return_to_pet_list(self):
        self.detail_frame.destroy()


#--------------------------------  
 
class Add_Pet:
  def __init__(self):
    self.add_pet = tk.Frame()

    # Labels
    self.pet_name = tk.Label(master=self.add_pet, text="Name: ")
    self.pet_gender = tk.Label(master=self.add_pet, text="Gender: ")
    self.pet_type = tk.Label(master=self.add_pet, text="Type: ")
    self.pet_breed = tk.Label(master=self.add_pet, text="Breed: ")
    self.pet_age = tk.Label(master=self.add_pet, text="Age: ")
    self.pet_img = tk.Label(master=self.add_pet, text="Img URL: ")
    self.pet_temperament = tk.Label(master=self.add_pet, text="Temperament: ")
    self.pet_date_broughtTo_shelter = tk.Label(master=self.add_pet, text="Date Brought To Shelter: ")
    self.pet_location = tk.Label(master=self.add_pet, text="Location: ")
    self.pet_status = tk.Label(master=self.add_pet, text="Status: ")


    #label grid
    self.pet_name.grid(row=0, column=0, pady=2)
    self.pet_gender.grid(row=1, column=0, pady=2)
    self.pet_type.grid(row=2, column=0, pady=2)
    self.pet_breed.grid(row=3, column=0, pady=2)
    self.pet_age.grid(row=4, column=0, pady=2)
    self.pet_img.grid(row=5, column=0, pady=2)
    self.pet_temperament.grid(row=6, column=0, pady=2)
    self.pet_date_broughtTo_shelter.grid(row=7, column=0, pady=2)
    self.pet_location.grid(row=8, column=0, pady=2)
    self.pet_status.grid(row=9, column=0, pady=2)

    #entry input
    self.pet_name_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_gender_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_type_input = ttk.Combobox(
      master=self.add_pet,
      state="readonly",
      values=["Cat", "Dog"],
      width=27                
    )
    self.pet_type_input.current(0)
    self.pet_breed_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_age_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_img_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_temperament_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_date_broughtTo_shelter_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_location_input = tk.Entry(master=self.add_pet, width=30)
    self.pet_status_input = ttk.Combobox(
      master=self.add_pet,
      state="readonly",
      values=["Available", "Not-Available"],
      width=27                
    )   
    #entry grid
    self.pet_name_input.grid(row=0, column=1, pady=2)
    self.pet_gender_input.grid(row=1, column=1, pady=2)
    self.pet_type_input.grid(row=2, column=1, pady=2)
    self.pet_breed_input.grid(row=3, column=1, pady=2)
    self.pet_age_input.grid(row=4, column=1, pady=2)
    self.pet_img_input.grid(row=5, column=1, pady=2)
    self.pet_temperament_input.grid(row=6, column=1, pady=2)
    self.pet_date_broughtTo_shelter_input.grid(row=7, column=1, pady=2)
    self.pet_location_input.grid(row=8, column=1, pady=2)
    self.pet_status_input.grid(row=9, column=1, pady=2)


    #buttons
    self.submit_button = tk.Button(
      master=self.add_pet,
      text="Submit",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.submit_form()
    )

    self.return_button = tk.Button(
      master=self.add_pet,
      text="Return",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.return_menu(currentFrame)
    )

    #error message
    self.error_msg = tk.Label(master=self.add_pet, fg="red")

    #success message
    self.scs_msg = tk.Label(master=self.add_pet, fg="green")

    self.submit_button.grid(row =10, column = 0, pady = 15)
    self.return_button.grid(row = 10, column = 1, pady = 15)
    self.error_msg.grid(row = 11, column = 0, columnspan=2, pady = 2)
    self.scs_msg.grid(row = 11, column = 0, columnspan=2, pady = 2)
    self.add_pet.pack()
  
  def submit_form(self):
    #msg = "Adding pets don't work at the moment. For testing data:\n"
    name = self.pet_name_input.get().strip()
    gender = self.pet_gender_input.get().strip()
    breed = self.pet_breed_input.get().strip()
    age = self.pet_age_input.get().strip()
    pet_type = self.pet_type_input.get().strip()
    img_url = self.pet_img_input.get().strip()
    temperament = self.pet_temperament_input.get().strip()
    date_brought_to_shelter = self.pet_date_broughtTo_shelter_input.get().strip()
    location = self.pet_location_input.get().strip()
    status = self.pet_status_input.get().strip()

    insert_pet(name, breed, pet_type, age, temperament, gender, date_brought_to_shelter, location, status, img_url)
    self.scs_msg.config(text="Pet details submitted successfully")
    self.add_pet.after(2000, lambda: self.scs_msg.config(text=""))
    
  def return_menu(self):
    cf = Admin_menu()
    self.add_pet.destroy()
  
#--------------------------------  

class Application:
    def __init__(self, parent, pet):
        self.parent = parent
        self.pet = pet

        self.application_frame = tk.Frame(self.parent)
        self.application_frame.pack()

        # Add labels and entry fields for user information
        self.name_label = tk.Label(self.application_frame, text="Name:")
        self.name_entry = tk.Entry(self.application_frame)
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)

        self.lname_label = tk.Label(self.application_frame, text="Last Name:")
        self.lname_entry = tk.Entry(self.application_frame)
        self.lname_label.grid(row=1, column=0)
        self.lname_entry.grid(row=1, column=1)

        self.adoption_date_label = tk.Label(self.application_frame, text="Adoption Date:")
        self.adoption_date_entry = tk.Entry(self.application_frame)
        self.adoption_date_label.grid(row=2, column=0)
        self.adoption_date_entry.grid(row=2, column=1)

        self.phone_label = tk.Label(self.application_frame, text="Phone:")
        self.phone_entry = tk.Entry(self.application_frame)
        self.phone_label.grid(row=3, column=0)
        self.phone_entry.grid(row=3, column=1)

        self.address_label = tk.Label(self.application_frame, text="Address:")
        self.address_entry = tk.Entry(self.application_frame)
        self.address_label.grid(row=4, column=0)
        self.address_entry.grid(row=4, column=1)

        # Submit button
        self.submit_button = tk.Button(self.application_frame, text="Submit", command=self.submit_application)
        self.submit_button.grid(row=5, columnspan=2)

    def submit_application(self):
        self.pet.status = "not-available"

        application_info = {
          adopted_pet: self.pet.id,# ----> Get the pet id from show_details
          #adopting_user: ,  ---> Figure out how to get username of current logged in user
          user_name: self.name_entry.get(),
          user_lname: self.lname_entry.get(),
          adoption_date: self.adoption_date_entry.get(),
          user_phone: self.phone_entry.get(),
          user_address: self.address_entry.get()
        }
        export_app_records(application_info)

        self.parent.remove_pet(self.pet)

#--------------------------------  
    #self made

class Template_menu:
  def __init__(self):
    self.frame = tk.Frame(window)

    #create widgets

    #self.widget.pack()

    #frame.pack()

  
  def return_func(self, cf):
    #example to return back to the previous menu/page
    cf = Login()
    self.destroy_self()
    
  def destroy_self(self):
    self.frame.destroy()

#--------------------------------  

# MAIN
  
#important
logo = """
Adopt me system
  ／l、    
（ﾟ､ ｡ ７    
l  ~ヽ  
  じしf_,)ノ
"""

window = tk.Tk()
window.geometry("800x600")

greeting = tk.Label(text=logo)
greeting.pack()

currentFrame = Menu()
window.mainloop()