from tkinter import *
import tkinter as tk

info_list = []


root = Tk()
root.geometry("350x350")
root.title("www.nike.com")

label1 = Label(root,text= "Sign up with Nike for exclusive discounts and more... ",foreground="white",bg= "black",padx= 150,pady=25, font= ("Ariel",10))
label1.pack(side=BOTTOM)

Tlabel = Label(root, text= "Nike ", fg= "orange",background="black",pady=15,padx=150,font=("Lato",24))
Tlabel.pack(side=TOP)

t2label = Label(root, text= "Just Do It ", fg= "orange",background="black",pady=5,padx=150,font=("Lato",16))
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


root.mainloop()