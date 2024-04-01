from tkinter import *
import sqlite3

def store_user_info(email, password):
    
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (email text, password text)''')
    
   
    c.execute("INSERT INTO users VALUES (?, ?)", (email, password))
    
  
    conn.commit()
    conn.close()

def validate_login(email, password):
    # Connect to the database
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    
    # Query the database for the provided email and password
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    
    # Close the connection
    conn.close()
    
    if user:
        return True
    else:
        return False

def login():
   
    email = textbox.get()
    password = textbox2.get()
    
    if validate_login(email, password):
        status_label.config(text="Login successful", fg="green")
    else:
        status_label.config(text="Email or password incorrect", fg="red")

root = Tk()
root.title("www.Nike.com")
root.geometry("350x350")

topLabel = Label(root, text="Nike Sign In Page", font=("ariel", 24), padx=50, pady=50, fg="orange", bg="orange", background="black")
topLabel.pack()

botLabel = Label(root, text="Just do it", font=("ariel", 24), fg="orange", bg="black", padx=150, pady=25)
botLabel.pack(side=BOTTOM)

label2 = Label(root, text="Enter email account: ")
label2.pack()

textbox = Entry(root)
textbox.pack()

labelpswrd1 = Label(root, text="Enter password: ")
labelpswrd1.pack()

textbox2 = Entry(root, show="*")  
textbox2.pack()

button = Button(root, text="Sign in", command=login)
button.pack()

status_label = Label(root, text="", fg="green")  
status_label.pack()

root.mainloop()
