from tkinter import *
import tkinter as tk
import re

root = Tk()
root.geometry("350x350")
root.title("www.Nike.com")

label1 = Label(root,text= "Sign up with Nike for exclusive discounts and more... ",foreground="white",bg= "black",padx= 150,pady=25, font= ("Ariel",10))
label1.pack(side=BOTTOM)

Tlabel = Label(root, text= "Nike ", fg= "orange",background="black",pady=15,padx=150,font=("Lato",34))
Tlabel.pack(side=TOP)

t2label = Label(root, text= "Just Do It ", fg= "white",background="black",pady=5,padx=150,font=("Lato",18))
t2label.pack(side=TOP)

label2 = Label(root,text= "Enter a vaild email account: ")
label2.pack()

textbox = Entry(root)
textbox.pack()


labelpswrd1 = Label(root, text= "Enter a password: ")
labelpswrd1.pack()

textbox2 = Entry(root)
textbox2.pack()

labelpswrd2 = Label(root, text= "Enter password again: ")
labelpswrd2.pack()

textbox1 = Entry(root)
textbox1.pack()

button = Button(root,text= "Create account")
button.pack()

def is_valid_email(email):
    # Regular expression for validating email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def create_account():
    email = textbox.get()  
    password1 = textbox2.get()  
    password2 = textbox1.get()  

    # Check if email is valid
    if not is_valid_email(email):
        print("Invalid email address. Please enter a valid email.")
        return

    # Checks if password is matches from prev input
    if password1 == password2:
        print("Email:", email)
        print("Password:", password1)
        
    else:
        print("Passwords do not match. Please try again.")

button = Button(root, text="Create account", command=create_account)

root.mainloop()