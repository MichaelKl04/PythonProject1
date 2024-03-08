import tkinter as tk
from tkinter import ttk

class Login:
  def __init__(self):
    self.frame = tk.Frame()

    self.userLabel = tk.Label(master=self.frame, text="User Name").pack()
    self.user = tk.Entry(master=self.frame, fg="white", bg="gray", width=30)
    self.user.pack()

    self.pwdLabel = tk.Label(master=self.frame, text="Password").pack()
    self.pwd = tk.Entry(master=self.frame, show="*",fg="white", bg="gray", width=30)
    self.pwd.pack()

    self.loginButton = tk.Button(
	  	master=self.frame,
	  	text="Login",
	  	width=25,
	  	bg="green",
	  	fg="yellow",
	  	command= lambda: self.log_in(),
	  ).pack(pady=15)

    self.err_msg = tk.Label(master=self.frame, fg="red").pack()

    self.frame.pack()

  def log_in(self):
    if(self.user.get() != 'admin' or self.pwd.get() != 'adopt'):
      self.err_msg.config(text="Invalid user or password.")
    else:
      Admin_menu()
      self.frame.destroy()

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
      command= lambda: self.display_pet_list()
    ).pack()

    self.add_pet = tk.Button(
      master=self.admin_menu,
      text="Add pet",
      width=25,
      bg="green",
      fg="yellow",
      
      command= lambda: self.display_add_pet()
    ).pack()

    self.remove_pet = tk.Button(
      master=self.admin_menu,
      text="Remove pet",
      width=25,
      bg="red",
      fg="yellow",
    ).pack()

    self.view_adoptions = tk.Button(
      master=self.admin_menu,
      text="View adoption applications",
      width=25,
      bg="red",
      fg="yellow",
    ).pack()

    self.logout = tk.Button(
      master=self.admin_menu,
      text="Logout",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.log_admin_out()
    )
    self.logout.pack()

    self.admin_menu.pack()

  # functions for each menu
  
  def display_pet_list(self):
    Pet_list()
    self.admin_menu.destroy()

  def display_add_pet(self):
    Add_Pet()
    self.admin_menu.destroy()
    
  def log_admin_out(self):
    Login()
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
      command= lambda: self.return_menu()
    )

    self.to_do.pack()
    self.return_button.pack()

    self.pet_list.pack()

  def return_menu(self):
    Admin_menu()
    self.pet_list.destroy()

#--------------------------------  
    
class Add_Pet:
  def __init__(self, data = None):
    self.add_pet = tk.Frame()

    names = ["Name: ", "Gender: ", "Type: ", "Breed: ", "Age: ", "Img URL: "]
    self.entries = []
    self.entries_labels = []
    
    for n in names:
      self.entries_labels.append(tk.Label(master=self.add_pet, text=n))
      if(n != "Type: "):
        self.entries.append(tk.Entry(master=self.add_pet, width=30))
      else:
        self.entries.append(ttk.Combobox(master=self.add_pet, state="readonly", values=["Cat", "Dog"], width=27))
        self.entries[2].current(0)
    
    for i in range(0, len(self.entries)):
      self.entries[i].grid(row = i, column = 1, pady = 2)
      
    for i in range(0, len(self.entries_labels)):
      self.entries_labels[i].grid(row = i, column = 0, pady = 2)
        
      
    if(data):
      for i in range(0, 6):
        if i != 2:
          self.entries[i].insert(0, data[i])
        else:
          self.entries[2].current(0 if data[2] == "Cat" else 1)
          


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
      command= lambda: self.return_menu()
    )

    #error message
    self.error_msg = tk.Label(master=self.add_pet, fg="red")

    self.submit_button.grid(row = 6, column = 0, pady = 15)
    self.return_button.grid(row = 6, column = 1, pady = 15)
    self.error_msg.grid(row = 7, column = 0, columnspan=2, pady = 2)
    self.add_pet.pack()
  
  def submit_form(self):
    post = []
    for e in self.entries:
      post.append(e.get())
      
    Add_Form(post)
    self.add_pet.destroy()

  def return_menu(self):
    Admin_menu()
    self.add_pet.destroy()
  
#--------------------------------  

class Add_Form:
  def __init__(self, data):
    
    self.add_remove_frame = tk.Frame(window)
    self.data = data
    self.data_labels = []
    self.data_values = []
    
    self.comfirm_label = tk.Label(master=self.add_remove_frame, text="Are you sure you want to add this pet?").grid(row=0, column=0, columnspan=2, pady=5)


    names = ["Name: ", "Gender: ", "Type: ", "Breed: ", "Age: ", "Img URL: "]
    
    #setting labels
    for n in names:
      self.data_labels.append(tk.Label(master=self.add_remove_frame, text=n))
    
    for d in self.data:
      self.data_values.append(tk.Label(master=self.add_remove_frame, text=d))
      
    #set grid
    for i in range(0, 6):
      self.data_labels[i].grid(row=(i+1), column=0, pady=5)
      self.data_values[i].grid(row=(i+1), column=1, pady=5)
      
    #button creation

    self.submit_button = tk.Button(
      master=self.add_remove_frame,
      text="Add",
      width=25,
      bg="green",
      fg="yellow",
    ).grid(row=7, column=0, pady=5)

    self.return_button = tk.Button(
      master=self.add_remove_frame,
      text="Cancel",
      width=25,
      bg="green",
      fg="yellow",
      command= lambda: self.return_form()
    ).grid(row=7, column=1, pady=5)
    
    #show the thing
    self.add_remove_frame.pack()
  
  def return_form(self):
    self.add_remove_frame.destroy()
    Add_Pet(self.data)


#--------------------------------  
    #self made

class Template_menu:
  def __init__(self):
    self.frame = tk.Frame(window)
  
  def return_func(self):
    Login()
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

Login()
window.mainloop()
