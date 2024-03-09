from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_info = website_entry.get()
    email_info = email_entry.get()
    pass_info = password_entry.get()

    if len(website_info) == 0 or len(email_info) == 0 or len(pass_info) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

    else:
        is_ok = messagebox.askokcancel(title=website_info,
                                       message=f"There are the details entered:\nEmail: {email_info}\n"
                                               f"Password: {pass_info}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_info} | {email_info} | {pass_info}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Generator")
window.config(padx=50, pady=50)

# Canvas Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels Setup
# Website Title Setup
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# Email Title Setup
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

# Password Title Setup
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries Setup
# Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email Entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "dex@gmail.com")

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons Setup
# Generate Password Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# Add Setup
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
