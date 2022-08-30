from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("750x450")
root.resizable(False, False)
root.title("BUZ Station")

#def


#Create
labTitle = ttk.Label(root, text = "BUZ Station", font=("impact", 60))
btnLaunch = ttk.Button(root, text = "Launch BUZ", padding = 20)


#Show
labTitle.pack()
btnLaunch.pack()


#loop
root.mainloop()