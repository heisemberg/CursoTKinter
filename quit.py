from tkinter import *

root = Tk()
root.title("Hola Mundo")

exit = Button(root, text="Salir", command=root.quit, fg="#eee", bg="gray")
exit.pack()

root.mainloop()