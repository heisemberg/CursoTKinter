from tkinter import *

root = Tk()
root.title("Calculadora")
root.configure(bg="#333333")
root.geometry("386x168")

equation = StringVar()

def press(num):
    equation.set(equation.get() + str(num))

def equalpress():
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set("error")

def clear():
    equation.set("")

# Configurar las columnas para que se expandan
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Configurar las filas para que se expandan
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

expression_entry = Entry(root, textvariable=equation, bg="#333333", fg="#eee") 
expression_entry.grid(row=0, columnspan=4, sticky="nsew")

btn7 = Button(root, text="7", bg="#666", fg="#fff", command=lambda: press(7))
btn7.grid(row=1, column=0, sticky="nsew")
btn8 = Button(root, text="8", bg="#666", fg="#fff", command=lambda: press(8))
btn8.grid(row=1, column=1, sticky="nsew")
btn9 = Button(root, text="9", bg="#666", fg="#fff", command=lambda: press(9))
btn9.grid(row=1, column=2, sticky="nsew")
btnsuma = Button(root, text="+", bg="#ff6600", fg="#fff", command=lambda: press("+"))
btnsuma.grid(row=1, column=3, sticky="nsew")
btn4 = Button(root, text="4", bg="#666", fg="#fff", command=lambda: press(4))
btn4.grid(row=2, column=0, sticky="nsew")
btn5 = Button(root, text="5", bg="#666", fg="#fff", command=lambda: press(5))
btn5.grid(row=2, column=1, sticky="nsew")
btn6 = Button(root, text="6", bg="#666", fg="#fff", command=lambda: press(6))
btn6.grid(row=2, column=2, sticky="nsew")
btnresta = Button(root, text="-", bg="#ff6600", fg="#fff", command=lambda: press("-"))
btnresta.grid(row=2, column=3, sticky="nsew")
btn1 = Button(root, text="1", bg="#666", fg="#fff", command=lambda: press(1))
btn1.grid(row=3, column=0, sticky="nsew")
btn2 = Button(root, text="2", bg="#666", fg="#fff", command=lambda: press(2))
btn2.grid(row=3, column=1, sticky="nsew")
btn3 = Button(root, text="3", bg="#666", fg="#fff", command=lambda: press(3))
btn3.grid(row=3, column=2, sticky="nsew")
btnmult = Button(root, text="*", bg="#ff6600", fg="#fff", command=lambda: press("*"))
btnmult.grid(row=3, column=3, sticky="nsew")
btn0 = Button(root, text="0", bg="#666", fg="#fff", command=lambda: press(0))
btn0.grid(row=4, column=0, columnspan=2, sticky="nsew")
btnpunto = Button(root, text=".", bg="#666", fg="#fff", command=lambda: press("."))
btnpunto.grid(row=4, column=2, sticky="nsew")
btndiv = Button(root, text="/", bg="#ff6600", fg="#fff", command=lambda: press("/"))
btndiv.grid(row=4, column=3, sticky="nsew")
btnclear = Button(root, text="Clear", bg="#666", fg="#fff", command=clear)
btnclear.grid(row=5, column=2, sticky="nsew")
btnequal = Button(root, text="=", bg="#ff6600", fg="#fff", command=equalpress)
btnequal.grid(row=5, column=3, sticky="nsew")

expression_entry.focus()
root.bind("<Return>", lambda x: equalpress())


root.mainloop()