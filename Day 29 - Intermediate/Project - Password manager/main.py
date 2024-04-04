from tkinter import *
from tkinter import messagebox
from generator import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web_site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web_site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        if messagebox.askokcancel(title=web_site, message=f"Are you sure and want to save this credentials?"):
            with open("pass_data.txt", "a") as data_file:
                data_file.write(f"{web_site} | {email} | {password}\n")
            password_entry.delete(0, END)
            website_entry.delete(0, END)

def gen_pass():
    password = generate_pass()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "petermoloch@mail.ru")
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
generate_pass_btn = Button(text="Generate Password", command=gen_pass)
generate_pass_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=45, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
