from tkinter import *


root = Tk()

root.title("www.Nike.com")
root.geometry("350x350")

topLabel = Label(root, text= "Nike Sign In Page", font= ("ariel", 24),padx= 50,pady=50,fg="orange", bg="orange", background= "black")
topLabel.pack()


botLabel = Label(root, text= "Just do it", font= ("ariel", 24),fg= "orange", bg= "black",padx= 150,pady=25)
botLabel.pack(side=BOTTOM)

label2 = Label(root,text= "Enter email account: ")
label2.pack()

textbox = Entry(root)
textbox.pack()


labelpswrd1 = Label(root, text= "Enter password: ")
labelpswrd1.pack()

textbox2 = Entry(root)
textbox2.pack()


button = Button(root,text= "Sign in")
button.pack()


root.mainloop()