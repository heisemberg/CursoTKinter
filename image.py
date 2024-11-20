from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hola Mundo")

# imagen = Image.open("img.jpg")
# imagen.show()

imagen = Image.open("img.jpg")
photo = ImageTk.PhotoImage(imagen)

l = Label(image=photo)
l.pack()

root.mainloop()