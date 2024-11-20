from tkinter import *

root = Tk()
root.title("Pies a Metros")

frame = Frame(root, padx=3, pady=12)
frame.grid(column=0, row=0)

def convertir():
    try:
        value = float(pies.get())
    except ValueError:
        metros.set("Por favor ingrese un número")
        return
    
    pies_value = float(pies.get())
    metros_value = pies_value * 0.3048
    metros.set(f"Es igual a {metros_value} metros")

pies = StringVar()
pies_input = Entry(frame, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
metros_output = Label(frame, textvariable=metros)
metros_output.grid(column=1, row=1)

Label(frame, text="Pies:").grid(column=0, row=0)

Button(frame, text="Convertir", command=convertir).grid(column=1, row=2)

pies_input.focus()
root.bind("<Return>", lambda x: convertir())


root.mainloop()