from tkinter import *

root =Tk()
root.title("Hola Mundo")
root.geometry("500x500")

e = Entry(root, width=40)
e.pack()
# e.insert(0, "Enter your name")

def click():
    hello = "Hello " + e.get()
    textvariable.set(hello)
    # l.configure(text=hello)
    e.delete(0, END)

btn = Button(root, text="Click me", command=click, fg="#eee", bg="gray")
btn.pack()

textvariable = StringVar()

l = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()