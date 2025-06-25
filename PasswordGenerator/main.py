from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate():
    #password_letters = [new_item for item in range(0,nr_letters-1)]

    password_entry.delete(0,END)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_letters)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)

    pyperclip.copy(password)
    #print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showerror(title = "Error",message=" You can't have empty fields")
    else:
        try :
            with open("data.json","r") as data_file:
                #Reading Old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating New Data
            data.update(new_data)
            with open("data.json","w") as data_file:
                # Reading Old Data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- WEBSITE SEARCH ------------------------------- #
def search ():
    website = website_entry.get().title()
    try :
        with open("data.json","r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message=" The Password List is EMPTY!")

    else:
        if website in data :
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}" + '\n' + f"Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f" No Data exists for {website}!")

    finally:
        website_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row = 0 , column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1,column=0)

email_label= Label(text="Email/Username")
email_label.grid(row=2,column=0)

password_label = Label(text="password")
password_label.grid(row=3,column=0)

#Entries
website_entry=Entry(width = 35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry= Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
#email_entry.insert(0,"yourmail@gmail.com")

password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)

#Buttons
generate_password= Button(text="Generate Password",command = generate)
generate_password.grid(row=3,column=2)

add_button = Button(text="Add",width = 36,command = save)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",command = search)
search_button.grid(row=1,column=2,columnspan=2)




window.mainloop()