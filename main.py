import random
# this imports all class and contants
from tkinter import *
#this imports messagebox which is itself another module
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    letter_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    symbol_list = [random.choice(symbols) for _ in range(random.randint(2,4))]
    number_list = [random.choice(numbers) for _ in range(random.randint(2,4))]
    
    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():

    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    
    if len(website_input)==0 or len(password_input) ==0:
        
        messagebox.showinfo(title="Incomplete Entry", message= "website or passowrd not provided.")
        
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: \nEmail: {email_input} \nPassword: {password_input} \n Is it ok to save ?")
        if is_ok:
            # Open the file in append & read mode ('a+')
            with open("password.tx", "a+") as file_object:
                # Move read cursor to the start of file.
                file_object.seek(0)
                # If file is not empty then append '\n'
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                # Append text at the end of file
                file_object.write(f"{website_input}  |  {email_input}  |  {password_input}")
            
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                email_entry.insert(0,"username@email.com")
                password_entry.delete(0,END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
lock_logo_img=PhotoImage(file="logo.png")
canvas.create_image(120,110,image=lock_logo_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_entry = Entry(width=38)
email_entry.insert(0, "myemail@email.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36,command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()