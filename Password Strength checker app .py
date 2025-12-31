from tkinter import *
import random
import string 
window = Tk() 
window.geometry('400x400') 
window.title('Password Strength Checker App') 
window.configure(bg='lightblue')
def generate_password():
    try:
        length = int(length_label_entry.get()) 
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        all = lower + upper + digits + symbols 
        password = ''.join(random.sample(all, length)) 
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    except ValueError:
        password_entry.delete(0, END)
        password_entry.insert(0, "Enter a valid number!")
length_label = Label(window, text='Enter Password Length:') 
length_label.pack(pady=10)
length_label_entry = Entry(window)
length_label_entry.pack(pady=5)
generate_btn = Button(window, text='Generate Password', command=generate_password) 
generate_btn.pack(pady=10) 
Label(window, text='Generated Password:').pack(pady=10)
password_entry = Entry(window, width=30) 
password_entry.pack(pady=5)
window.mainloop()
