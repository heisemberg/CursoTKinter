from tkinter import *

root = Tk()
root.title("Hola Mundo")
root.geometry("500x500")

l = Label(root, text="Button clicked")
def click():
    l.pack()

btn = Button(root, text="Click me", command=click, fg="#eee", bg="gray")
btn.pack()


root.mainloop()