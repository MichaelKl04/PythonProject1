import tkinter as tk
from tkinter import ttk

currentFrame = None

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

    self.err_msg = tk.Label(master=self.frame, fg="red")

    self.userLabel.pack()
    self.user.pack()
    self.pwdLabel.pack()
    self.pwd.pack()
    self.loginButton.pack(pady=15)
    self.err_msg.pack()

    self.frame.pack()

  def destroy_self(self):
    self.frame.destroy()

  def log_in(self, cf):
    if(self.user.get() != 'admin' or self.pwd.get() != 'adopt'):
      self.err_msg.config(text="Invalid user or password.")
    else:
      cf = Admin_menu()
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
    self.pet_list = tk.Frame(window)
    self.to_do = tk.Label(master=self.pet_list, text="This is the part where you attempt to look for pets in the SQL database")
    self.return_button = tk.Button(
      master=self.pet_list,
      text="Return",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.return_menu(currentFrame)
    )

    self.to_do.pack()
    self.return_button.pack()

    self.pet_list.pack()

  def return_menu(self, cf):
    cf = Admin_menu()
    self.pet_list.destroy()

#--------------------------------  
    
class Add_Pet:
  def __init__(self, name = None, gender = None, breed = None, age = None, img_url = None):
    self.add_pet = tk.Frame()

    #label
    self.pet_name = tk.Label(master=self.add_pet, text="Name: ")
    self.pet_gender = tk.Label(master=self.add_pet, text="Gender: ")
    self.pet_type = tk.Label(master=self.add_pet, text="Type: ")
    self.pet_breed = tk.Label(master=self.add_pet, text="Breed: ")
    self.pet_age = tk.Label(master=self.add_pet, text="Age: ")
    self.pet_img = tk.Label(master=self.add_pet, text="Img URL: ")

    #label grid
    self.pet_name.grid(row = 0, column = 0, pady = 2)
    self.pet_gender.grid(row = 1, column = 0, pady = 2)
    self.pet_type.grid(row = 2, column = 0, pady = 2)
    self.pet_breed.grid(row = 3, column = 0, pady = 2)
    self.pet_age.grid(row = 4, column = 0, pady = 2)
    self.pet_img.grid(row = 5, column = 0, pady = 2)

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

    #check for parameters
    if name:
      self.pet_name_input.insert(0, name)

    if gender:
      self.pet_gender_input.insert(0, gender)

    if breed:
      self.pet_breed_input.insert(0, breed)

    if age:
      self.pet_age_input.insert(0, age)

    if img_url:
      self.pet_img_input.insert(0, img_url)
  
    #entry grid
    self.pet_name_input.grid(row = 0, column = 1, pady = 2)
    self.pet_gender_input.grid(row = 1, column = 1, pady = 2)
    self.pet_type_input.grid(row = 2, column = 1, pady = 2)
    self.pet_breed_input.grid(row = 3, column = 1, pady = 2)
    self.pet_age_input.grid(row = 4, column = 1, pady = 2)
    self.pet_img_input.grid(row = 5, column = 1, pady = 2)
    


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

    self.submit_button.grid(row = 6, column = 0, pady = 15)
    self.return_button.grid(row = 6, column = 1, pady = 15)
    self.error_msg.grid(row = 7, column = 0, columnspan=2, pady = 2)
    self.add_pet.pack()
  
  def submit_form(self):
    cf = Add_Remove_Form(
      "Add", 
      self.pet_name_input.get(),
      self.pet_gender_input.get(),
      self.pet_type_input.get(),
      self.pet_breed_input.get(),
      self.pet_age_input.get(),
      self.pet_img_input.get()
    )
    self.add_pet.destroy()

  def return_menu(self, cf):
    cf = Admin_menu()
    self.add_pet.destroy()
  

#--------------------------------  

class Add_Remove_Form:
  def __init__(self, mode, name, gender, pet_type, breed, age, img_url):

    #text variables
    
    self.name = name
    self.gender = gender
    self.type = pet_type
    self.breed = breed
    self.age = age
    self.img = img_url

    #frames

    self.add_remove_frame = tk.Frame(window)

    self.comfirm_label = tk.Label(master=self.add_remove_frame, text="Are you sure you want to add this pet?")
    self.comfirm_label.grid(row=0, column=0, columnspan=2, pady=5)

    # labels
    self.name_label = tk.Label(master=self.add_remove_frame, text="Name: ")
    self.gender_label = tk.Label(master=self.add_remove_frame, text="Gender: ")
    self.type_label = tk.Label(master=self.add_remove_frame, text="Type: ")
    self.breed_label = tk.Label(master=self.add_remove_frame, text="Breed: ")
    self.age_label = tk.Label(master=self.add_remove_frame, text="Age: ")
    self.img_label = tk.Label(master=self.add_remove_frame, text="Img URL: ")

    self.name_value = tk.Label(master=self.add_remove_frame, text=name)
    self.gender_value = tk.Label(master=self.add_remove_frame, text=gender)
    self.type_value = tk.Label(master=self.add_remove_frame, text=pet_type)
    self.breed_value = tk.Label(master=self.add_remove_frame, text=breed)
    self.age_value = tk.Label(master=self.add_remove_frame, text=age)
    self.img_value = tk.Label(master=self.add_remove_frame, text=img_url)   

    #button

    self.submit_button = tk.Button(
      master=self.add_remove_frame,
      text="Add",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.add()
    )

    self.return_button = tk.Button(
      master=self.add_remove_frame,
      text="Cancel",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.return_form(currentFrame)
    )

    #grid 

    self.name_label.grid(row=1, column=0, pady=5)
    self.gender_label.grid(row=2, column=0, pady=5)
    self.type_label.grid(row=3, column=0, pady=5)
    self.breed_label.grid(row=4, column=0, pady=5)
    self.age_label.grid(row=5, column=0, pady=5)
    self.img_label.grid(row=6, column=0, pady=5)

    self.name_value.grid(row=1, column=1, pady=5)
    self.gender_value.grid(row=2, column=1, pady=5)
    self.type_value.grid(row=3, column=1, pady=5)
    self.breed_value.grid(row=4, column=1, pady=5)
    self.age_value.grid(row=5, column=1, pady=5)
    self.img_value.grid(row=6, column=1, pady=5)
    
    self.submit_button.grid(row=7, column=0, pady=5)
    self.return_button.grid(row=7, column=1, pady=5)

    self.add_remove_frame.pack()
  
  def return_form(self, cf):
    self.add_remove_frame.destroy()
    cf = Add_Pet(
      self.name,
      self.gender,
      self.breed,
      self.age,
      self.img
    )


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

currentFrame = Login()
window.mainloop()
