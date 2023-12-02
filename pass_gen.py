from tkinter import *
from tkinter import messagebox
import secrets
import string



window = Tk()

window.configure(background = "#e9e2a1")

window.title("Password Generator")
window.resizable(0, 0) 
window.geometry("550x600")


def generate_button():

    # get length from user
    len = length_txt.get()

    if int(len) <= 8:
        length_txt.delete(0, END)
        password_txt.delete(0, END)
        messagebox.showerror("Error","Length must be > 8")
        return
    
    # generate string with all alphabets, digits, special char
    password_temp = string.ascii_uppercase + string.digits + string.ascii_lowercase +  string.punctuation

    # generate N len of string by secrets.choice from password_temp
    password = ''.join(secrets.choice(password_temp) for i in range(int(len)))  # for a 20-character password

    #clear password text area 
    password_txt.delete(0, END)

    # insert new value in password txt area
    password_txt.insert(INSERT, password)




#Top header
label_heading = Label(window, text = "Password Generator", font=("Helvetica", 20,'bold'),background='#55C1E6')

length_label = Label(window, text = "Enter the length of the password you want: ", font=("Helvetica", 15),background='#E6DDBB')


length_txt = Entry(window, font=('Helvetica',10,'bold'), width=10,)

generate_button = Button(window, text = "Generate", fg = "black", bg = "#55C1E6", command = generate_button)



password_txt = Entry(window, font=('Helvetica',10,'bold'), width=12,)


label_heading.grid(row = 2, column = 3, pady=20)

length_label.grid(row=3, column=3,pady=20)

length_txt.grid(row=3, column=4,padx=1,pady=4,ipadx=10)

password_txt.grid(row=4, column=3,ipadx=30,ipady=5, pady=20)

generate_button.grid(row=4, column=2,ipady=12, pady=20)

window.mainloop()
