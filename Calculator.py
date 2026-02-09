import tkinter as tk
import math
class  ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.configure(bg="#ffc0cb")
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10, ipady=10)
        self.create_buttons()
    def click_button(self, value):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + value)
    def clear_button(self):
        self.display.delete(0, tk.END)
    def equal_button(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    def scientific_function(self, func):
        try:
            expr = self.display.get()
            if expr == "":
                return
            value = eval(expr)
            result = getattr(math, func)(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    def insert_constant(self, const):
        self.click_button(str(getattr(math, const)))
    def create_buttons(self):
        buttons = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3), ("sin",1,4), ("cos",1,5),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3), ("tan",2,4), ("log",2,5),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3), ("sqrt",3,4), ("exp",3,5),
            ("0",4,0), (".",4,1), ("+",4,2), ("=",4,3), ("pi",4,4), ("C",4,5),
        ]
        for (text, row, col) in buttons:
            if text == "=":
                action = self.equal_button
            elif text == "C":
                action = self.clear_button
            elif text in ["sin", "cos", "tan", "log", "sqrt", "exp"]:
                action = lambda f=text: self.scientific_function(f)
            elif text in ["pi"]:
                action = lambda c=text: self.insert_constant(c)
            else:
                action = lambda val=text: self.click_button(val)
            tk.Button(self.root, text=text, width=6, height=2, font=("Arial", 14),
                      bg="#ff69b4", fg="white", command=action).grid(row=row, column=col, padx=5, pady=5)
if __name__ == "__main__":
    root = tk.Tk()
    ScientificCalculator(root)
    root.mainloop()