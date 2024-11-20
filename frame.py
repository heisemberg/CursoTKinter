from tkinter import *

root = Tk()
root.title("Hola Mundo")

#frame = LabelFrame(root, text="Login", padx=50, pady=50)
#frame = LabelFrame(root, padx=50, pady=50, borderwidth=10, relief="sunken")
frame = Frame(root, padx=50, pady=50)
frame.pack(padx=100, pady=100)


l = Label(frame, text="Button clicked")
btn = Button(frame, text="Salir", command=root.quit, fg="#eee", bg="gray")
l.pack()
btn.pack()


root.mainloop() 