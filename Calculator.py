import tkinter as tk
from tkinter import *

string_Value = ""
def add_calculation(val):
    global string_Value
    string_Value += str(val)
    result.delete(1.0, "end")
    result.insert(1.0, string_Value)

def del_calculation():
    global string_Value
    string_Value = list(string_Value)
    try:
        string_Value.pop()
    except:
        pass
    string_Value = ''.join(string_Value)
    result.delete(1.0, "end")
    result.insert(1.0, string_Value)

def eval_calculation():
    global string_Value
    try:
        string_Value = str(eval(string_Value))
        result.delete(1.0, "end")
        result.insert(1.0, string_Value)
    except:
        clear_text()
        result.insert(1.0, "Error!")
    
def clear_text():
    global string_Value
    string_Value = ""
    result.delete(1.0, "end")

window = tk.Tk()
window.configure(bg='#FFFFFF')
window.iconphoto(False,PhotoImage(file = 'calculatrice.png'))
window.title("Calculatrice")
window.geometry("335x277")
result = tk.Text(window, height=2, width=19, font=("Arial", 24))
result.grid(columnspan=5)

btn1 = tk.Button(window, text="1", command=lambda: add_calculation(1), width=6, font=("Arial", 15))
btn1.grid(row=2, column=0)

btn2 = tk.Button(window, text="2", command=lambda: add_calculation(2), width=6, font=("Arial", 15))
btn2.grid(row=2, column=1)

btn3 = tk.Button(window, text="3", command=lambda: add_calculation(3), width=6, font=("Arial", 15))
btn3.grid(row=2, column=2)

btn4 = tk.Button(window, text="4", command=lambda: add_calculation(4), width=6, font=("Arial", 15))
btn4.grid(row=3, column=0)

btn5 = tk.Button(window, text="5", command=lambda: add_calculation(5), width=6, font=("Arial", 15))
btn5.grid(row=3, column=1)

btn6 = tk.Button(window, text="6", command=lambda: add_calculation(6), width=6, font=("Arial", 15))
btn6.grid(row=3, column=2)

btn7 = tk.Button(window, text="7", command=lambda: add_calculation(7), width=6, font=("Arial", 15))
btn7.grid(row=4, column=0)

btn8 = tk.Button(window, text="8", command=lambda: add_calculation(8), width=6, font=("Arial", 15))
btn8.grid(row=4, column=1)

btn9 = tk.Button(window, text="9", command=lambda: add_calculation(9), width=6, font=("Arial", 15))
btn9.grid(row=4, column=2)


btn_del = tk.Button(window, text="Del", command=lambda: del_calculation(), width=6, font=("Arial", 15), bg="gray")
btn_del.grid(row=2, column=3)

btn_moi = tk.Button(window, text="+", command=lambda: add_calculation("+"), width=6, font=("Arial", 15),bg="gray")
btn_moi.grid(row=3, column=3)

btn_mult = tk.Button(window, text="-", command=lambda: add_calculation("-"), width=6, font=("Arial", 15),bg="gray")
btn_mult.grid(row=4, column=3)

btn_div = tk.Button(window, text="x", command=lambda: add_calculation("*"), width=6, font=("Arial", 15),bg="gray")
btn_div.grid(row=5, column=3)

btn_div = tk.Button(window, text="/", command=lambda: add_calculation("/"), width=6, font=("Arial", 15),bg="gray")
btn_div.grid(row=6, column=3)

btn_openBra = tk.Button(window, text="=", command= eval_calculation, width=14, font=("Arial", 15), bg="cyan")
btn_openBra.grid(row=6, column=0,columnspan=2)

btn_closeBra = tk.Button(window, text="0", command=lambda: add_calculation("0"), width=6, font=("Arial", 15))
btn_closeBra.grid(row=5, column=2)

btn_clear = tk.Button(window, text="C", command=clear_text, width=14,font=("Arial", 15) ,bg="orange")
btn_clear.grid(row=5, column=0,columnspan=2)

btn_equ = tk.Button(window, text=".", command=lambda: add_calculation("."), width=6, font=("Arial", 15))
btn_equ.grid(row=6, column=2)


window.mainloop()