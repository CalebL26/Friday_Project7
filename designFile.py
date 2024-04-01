from tkinter import *
import tkinter as tk
import re
import sqlite3

def validate_email(email):
    # Regular expression pattern for validating email address
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

def validate_password(password1, password2):
    # Check if the passwords match
    if password1 == password2:
        return True
    else:
        return False

def store_user_info(email, password):
    # Connect to the database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (email text, password text)''')
    
    # Insert user's information into the database
    c.execute("INSERT INTO users VALUES (?, ?)", (email, password))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def submit():
    # Get user input from textboxes
    email = textbox.get()
    password1 = textbox1.get()
    password2 = textbox2.get()
    
    # Validate email and passwords
    if validate_email(email) and validate_password(password1, password2):
        # Store user's information in the database
        store_user_info(email, password1)
        print("User signed up successfully!")
    else:
        print("Invalid email address or passwords do not match!")

root = Tk()
root.geometry("450x450")
root.title("www.Nike.com")

label1 = Label(root,text= "Sign up with Nike for exclusive discounts and more... ",foreground="white",bg= "black",padx= 100,pady=10, font= ("Ariel",10))
label1.pack(side=BOTTOM)

Tlabel = Label(root, text= "Nike ", fg= "orange",background="black",pady=10,padx=250,font=("Lato",34))
Tlabel.pack(side=TOP)

t2label = Label(root, text= "Just Do It ", fg= "white",background="black",pady=5,padx=250,font=("Lato",18))
t2label.pack(side=TOP)

label2 = Label(root,text= "Enter a valid email account: ")
label2.pack()

textbox = Entry(root)
textbox.pack()


labelpswrd1 = Label(root, text= "Enter a password: ")
labelpswrd1.pack()

textbox1 = Entry(root, show="*")
textbox1.pack()

labelpswrd2 = Label(root, text= "Re-enter password: ")
labelpswrd2.pack()

textbox2 = Entry(root, show="*")
textbox2.pack()

button = Button(root,text= "Create account", command=submit)
button.pack()

root.mainloop()
