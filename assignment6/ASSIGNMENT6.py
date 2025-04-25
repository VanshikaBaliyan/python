import tkinter as tk
from tkinter import messagebox

class Calculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
    
        self.display_var = tk.StringVar()
        self.display = tk.Entry(root, textvariable=self.display_var, 
                               font=('Arial', 20), bd=10, insertwidth=2,
                               width=14, borderwidth=4, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Creating buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 15),
                     command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def on_button_click(self, button):
        current_text = self.display_var.get()
        
        if button == 'C':
            self.display_var.set('')
        elif button == '=':
            try:
                result = eval(current_text)
                self.display_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.display_var.set('')
        else:
            self.display_var.set(current_text + button)

if __name__ == "_main_":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()