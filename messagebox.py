from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hola Mundo")

# def click():
#     messagebox.showinfo("Hola Mundo", "Button clicked")

# def click():
#     messagebox.showwarning("Hola Mundo", "Button clicked")

# def click():
#      messagebox.showerror("Hola Mundo", "Button clicked")

""" def click():
    respuesta=messagebox.askquestion("Hola Mundo", "Button clicked") 
    if respuesta == "yes":
        respuesta=True
    else:
        respuesta=False
    
    return respuesta

print(click()) """

""" def click():
    messagebox.askokcancel("Hola Mundo", "Button clicked")
    if True:
        print("ok")
    else:
        print("cancel") """

def click():
    messagebox.askyesno("Hola Mundo", "Button clicked")
    if True:
        print("ok")
    else:
        print("cancel")

btn =Button(root, text="presioname", command = click)
btn.pack()

root.mainloop()