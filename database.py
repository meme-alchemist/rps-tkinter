import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('userentry.db')

c = conn.cursor()
#table for now
c.execute("""CREATE TABLE IF NOT EXISTS users
             (username TEXT UNIQUE NOT NULL,
             password TEXT CHECK(LENGTH(password) >= 8 AND LENGTH(password) <= 20) NOT NULL)
        """)

conn.commit()

def register():
    username = username_entry.get()
    password = password_entry.get()

    if len(password) < 8 or len(password) > 20:
        messagebox.showerror("Registration Failed", "Password length must be between 8 and 20 characters.")
        return

    # Check if username already exists in the database
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone() is not None:
        messagebox.showerror("Registration Failed", "Username already exists.")
        return

    # Insert the new user credentials into the database
    c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
    conn.commit()

    messagebox.showinfo("Registration Successful", "You have successfully registered.")

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if username and password match in the database
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone() is not None:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = tk.Tk()
root.title("Login/Register")

#entry
username_label = tk.Label(root, text = "username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)

password_label = tk.Label(root, text= "password")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(root, show = "*")
password_entry.grid(row=2, column=1)

#register
register_button = tk.Button(root, text="Register", command=register)
register_button.grid(row=3, column=1, columnspan=2)

#login
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=4, column=1, columnspan=2)

root.mainloop()

c.close()
conn.close()