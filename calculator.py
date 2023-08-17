import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_label = ttk.Label(root, textvariable=self.result_var, font=("Helvetica", 20), anchor="e")
        self.result_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        self.row_index = 1
        self.col_index = 0
        for button_text in self.buttons:
            ttk.Button(root, text=button_text, command=lambda text=button_text: self.on_button_click(text)).grid(row=self.row_index, column=self.col_index, padx=5, pady=5)
            self.col_index += 1
            if self.col_index > 3:
                self.col_index = 0
                self.row_index += 1

    def on_button_click(self, text):
        if text == '=':
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            if current_text == '0' and text != '.':
                self.result_var.set(text)
            else:
                self.result_var.set(current_text + text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
