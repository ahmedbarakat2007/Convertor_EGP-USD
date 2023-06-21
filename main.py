import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import webbrowser

root = Tk()
root.geometry ('450x530') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.iconbitmap("Textures\icon.ico")
menubar = Menu(root, background="#16191f", foreground="white")
root.configure(bg="#005a75")
root.config(menu=menubar)

def about():
    hi = Tk()
    hi.geometry("300x150")
    hi.resizable(0,0)
    hi.configure(bg="#005a75")
    def github():
        webbrowser.open("https://www.github.com/ahmedbarakat2007")
    
    Label(hi, text="",bg="#005a75").pack()
    Label(hi, text="Convertor USD - EGP", font='san-serif 14 bold',bg="#005a75",fg="white").pack()
    Label(hi, text="",bg="#005a75").pack()
    Label(hi, text="Made by Ahmed Barakat", font='san-serif 10 bold',bg="#005a75",fg="white").pack()
    Label(hi, text="",bg="#005a75",borderwidth=0).pack()
    Button(hi, text = "Github", command= github,bg="#2b686e", fg="white", borderwidth=0).pack()
    hi.mainloop()

# create a menu
file_menu = Menu(menubar)
file_menu.add_command(
    label='About',
    command=about
)

file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

root.title('EGP - USD Convertor (Made by Ahmed Barakat)')
def convert():
    try:
        gtr =float(a.get())
        c = gtr * 30
        msg = messagebox.showinfo("Completed!! Converting From USD to EGP", c)
    except:
        msg1 = messagebox.showerror("ERROR!!!", "Something Went Wrong")
def convert1():
    try:
        gtr =float(a1.get())
        c = gtr / 30
        msg = messagebox.showinfo("Completed!! Converting From EGP to USD", c)
    except:
        msg1 = messagebox.showerror("ERROR!!!", "Something Went Wrong")

Label(root, text="",bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()

img = Image.open('Textures\icon.png')
img = img.resize((75, 70), Image.ANTIALIAS)    
img = ImageTk.PhotoImage(img)
panel = Label(root, image=img,bg="#005a75")
panel.image = img
panel.pack(side = "top", expand = "no")

Label(root, text="",bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()

Label(root, text = "Convertor From USD to EGP",bg="#005a75", fg="white", font='san-serif 14 bold').pack()
Label(root, text="",bg="#005a75").pack()
a = Entry(root)
a.insert(0, "USD")
a.pack()
Label(root, text="",bg="#005a75").pack()
submit = Button(root, text = "Convert to EGP", command= convert,borderwidth=0,bg="#2b686e", fg="white").pack()

Label(root, text="",bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()

Label(root, text = "Convertor From EGP to USD", fg="white", font='san-serif 14 bold',bg="#005a75").pack()
Label(root, text="",bg="#005a75").pack()
a1 = Entry(root)
a1.insert(0, "EGP")
a1.pack()
Label(root, text="",bg="#005a75").pack()
submit1 = Button(root, text = "Convert to USD", command= convert1,borderwidth=0,bg="#2b686e", fg="white").pack()

root.mainloop()
