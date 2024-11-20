from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.geometry("500x500")

label1 = Label(root, text="Hola Mundo! mi primera etiqueta")
label2 = Label(root, text="Hola Mundo! mi primera etiqueta")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)


root.mainloop()