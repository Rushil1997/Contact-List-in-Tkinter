from tkinter import *
from tkinter import messagebox


# _______________________________________Button Functionality  ____________________________________________________
def add_contact():
    name = name_entry.get()
    number = cell_entry.get()
    email = email_entry.get()
    if len(number) > 10 or len(number) == 0:
        messagebox.showwarning(title="Invalid Number", message="A cell number has a maximum of 10 digits ")
    elif len(name) == 0:
        messagebox.showwarning(title="Invalid Name", message=" The contact name field can not be empty  ")
    elif len(email) == 0:
        messagebox.showwarning(title="Invalid Email", message=" The email field can not be empty  ")
    else:
        with open("contacts.txt", "a") as file:
            file.write(f"\n Contact Name: {name} | Cell Number: {number} | Email: {email}")
            name_entry.delete(0, END)
            cell_entry.delete(0, END)
            email_entry.delete(0, END)
        messagebox.showinfo(title="Added", message="Contact Has been added ")


# _______________________________________GUI Interface ____________________________________________________
# Creating the window
window = Tk()
window.title("Contact List")
window.config(padx=50, pady=50)

# Creating a canvas // If you want an image to be added to the program

# canvas = Canvas(width=200, height=200)
# img = PhotoImage(file="logo.jpeg")
# canvas.create_image(10,10,image=img)
# canvas.grid(row=0, column =0)


# Creating name label
name_label = Label(text="Contact Name:", fg="blue", font=("Arial", 12))
name_label.grid(row=1, column=0)
# Creating  name Entry

name_entry = Entry(width=24)
name_entry.grid(row=1, column=1)

# Creating cell no label
cell_label = Label(text="Cell Number:", fg="blue", font=("Arial", 12))
cell_label.grid(row=2, column=0)

# Creating  Cell no  Entry
cell_entry = Entry(width=24)
cell_entry.grid(row=2, column=1)
# Creating email label
email_label = Label(text="Email", fg="blue", font=("Arial", 12))
email_label.grid(row=3, column=0)

# Creating  name Entry
email_entry = Entry(width=24)
email_entry.grid(row=3, column=1)

# Add Button
add = Button(text="Add", width=36, command=add_contact)
add.grid(row=5, column=0, columnspan=3)

window.mainloop()
