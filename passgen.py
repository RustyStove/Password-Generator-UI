import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import string
import random

def is_integer(num):
    return isinstance(num, int)

def passwordgen():
    numlength = int(entryName.get())
    password = []
    characterList = []
    c1 = var.get()
    c2 = var2.get()
    c3 = var3.get()
    #find out how to check the checkbox state and add randomizarion code in elif and find out how to stop enter letters
    if is_integer(numlength) and numlength > 0:
        #messagebox.showinfo("Password", "length= " + str(numlength) +" "+ str(c1)+ str(c2)+ str(c3))
        if c1 == 1:
            characterList += string.digits
        if c2 == 1:
            characterList += string.ascii_letters
        if c3 == 1:
            characterList += string.punctuation
        
        for i in range(numlength):
            randomchar = random.choice(characterList)
     
            password.append(randomchar)
            finalpass = "".join(password)

        messagebox.showinfo("Password", "Your Password is "+ str(finalpass) +
                            "\n Your password has been copied to the clipboard.")
        app.withdraw()
        app.clipboard_clear()
        app.clipboard_append(finalpass)
        app.update

    elif numlength == 0:
        messagebox.showinfo("Password", "Length cannot be 0")
    else:
        messagebox.showinfo("Password", "Please enter a length and/or select an element")



if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("560x270")
    var = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    label = tk.Label(app, text="Password Generator")
    app.columnconfigure(0, weight=1)
    app.columnconfigure(1, weight=1)
    app.columnconfigure(2, weight=1)
    label.grid(row=0, column=1)
    app.title("Password Generator")

    lsum = tk.Label(app, text = 'Enter desired length and elements')
    lsum.grid(row=1, column=1, pady=4)

    labelName = tk.Label(app, text="Length:")
    labelName.grid(row=3, column=1, padx=15, pady=10)
    entryName = tk.Entry(app, justify="center")
    entryName.grid(row=4, column=1, padx=15, pady=0)

    checktext = tk.Label(app, text="Select Elements:")
    checktext.grid(row=5, column=1, padx=15, pady=10)
    c1 = ttk.Checkbutton(app, text='Numbers', variable=var)
    c1.grid(row=6, column=0, padx=5, pady=0)

    c2 = ttk.Checkbutton(app, text='Letters', onvalue=1, offvalue=0, variable=var2)
    c2.grid(row=6, column=1, padx=5, pady=0)

    c3 = ttk.Checkbutton(app, text='Special Characters', onvalue=1, offvalue=0,variable=var3)
    c3.grid(row=6, column=2, padx=5, pady=0)

    buttonGet = tk.Button(app, text="Generate Password", command=passwordgen)
    buttonGet.grid(row=7, column=1, padx=15, pady=8, sticky="we")
    
    app.mainloop()