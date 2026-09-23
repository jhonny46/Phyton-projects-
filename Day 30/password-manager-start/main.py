from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from tkinter.messagebox import showinfo

from pyexpat.errors import messages
import pyperclip
import json


FONT = "Arial"
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters =randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters)for _ in range(nr_letters)]
    password_symbols = [choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [choice(numbers)for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pass_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = pass_text.get()

#POP UP MESSAGE BOX
    new_data = {
        website : {
            "email": email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo( title = "Oops", message=" Please make sure to put in password and website" )

    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading Json file
                data =  json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)

        else:
                #updateing Jason file
            data.update(new_data)

            with open("data.json", "w") as data_file:
            # saving updated data
                 json.dump(data, data_file, indent=4)

        finally:
            website_text.delete(0,END)
            pass_text.delete(0,END)

def search_password():
    website = website_text.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title= "Error",  message= "No data file is found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Notfound", message=f"Website {website} not found")





            # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

logo = PhotoImage(file = "logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100, 100, image = logo)
canvas.grid( row= 0 , column = 1)

# Lables
website = Label(text = "Website:" )
website.grid(row= 1, column= 0)
email_lable = Label(text = "Email:")
email_lable.grid(row =2, column = 0)
pass_label = Label(text = "Password:")
pass_label.grid(row = 3, column = 0)

#---- Inputs___
website_text = Entry(width= 25, bg = "white", fg= "black")
website_text.grid(row = 1, column= 1, )
website_text.focus()
email_text = Entry(width=35, bg = "white", fg= "black")
email_text.grid(row=2, column = 1, columnspan= 2)
email_text.insert(0, "Johnny@gmail.com") # Pre filled dummy email
pass_text = Entry(width= 25, bg = "white", fg= "black")
pass_text.grid(row=3, column= 1)

# Buttons
search_button = Button(text="Search", width = 13, command= search_password)
search_button.grid(row=1, column= 2)

gen_pass = Button(text="Generate Password", command= generate_pass)
gen_pass.grid(row =3 , column= 2, columnspan=2)

add_button = Button(text="Add", width = 36, command= save)
add_button.grid(row=4, column= 1, columnspan= 2)


window.mainloop()