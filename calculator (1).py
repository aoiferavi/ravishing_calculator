import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Ravishing Calculator")

        # Create Entry widget to display input/output
        
        self.display = tk.Entry(master, width=35, borderwidth=5, fg="black", bg="#F5F5F5", font=("Arial", 11))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Create buttons
        self.button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9), bg="#FFFFFF", fg="black", font=("Arial", 14))
        self.button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0), bg="#FFFFFF", fg="black", font=("Arial", 14))

        self.button_add = tk.Button(master, text="+", padx=41, pady=20, command=lambda: self.button_operation("+"), bg="#FFA500", fg="black", font=("Arial", 14))
        self.button_subtract = tk.Button(master, text="-", padx=43, pady=20, command=lambda: self.button_operation("-"), bg="#FFA500", fg="black", font=("Arial", 14))
        self.button_multiply = tk.Button(master, text="*", padx=41, pady=20, command=lambda: self.button_operation("*"), bg="#FFA500", fg="black", font=("Arial", 14))
        self.button_divide = tk.Button(master, text="/", padx=42, pady=20, command=lambda: self.button_operation("/"), bg="#FFA500", fg="black", font=("Arial", 14))
        self.buttonequal = tk.Button(master, text="=", padx=147, pady=20, command=self.button_equal, bg="#FFA500", fg="black", font=("Arial", 14))
        self.buttonclear = tk.Button(master, text="C", padx=38, pady=20, command=self.button_clear, bg="#FFA500", fg="black", font=("Arial", 14))
        
        
        

        # Put buttons on the screen
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)

        self.button_0.grid(row=4, column=1)
        self.buttonclear.grid(row=4, column=0)
        self.button_divide.grid(row=4, column=2)

        self.button_add.grid(row=5, column=0)
        self.button_subtract.grid(row=5, column=1)
        self.button_multiply.grid(row=5, column=2)

        self.buttonequal.grid(row=6, column=0, columnspan=3)


    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(number))

    def button_clear(self):
        self.display.delete(0, tk.END)

    def button_operation(self, operation):
        self.first_number = self.display.get()
        self.operation = operation
        self.display.delete(0, tk.END)

    def cancel(self):
        self.display.delete(0, tk.END)

    def button_equal(self):
        second_number = self.display.get()
        self.display.delete(0, tk.END)

        if self.operation == "+":
            self.display.insert(0, int(self.first_number) + int(second_number))
        elif self.operation == "-":
            self.display.insert(0, int(self.first_number) - int(second_number))
        elif self.operation == "*":
            self.display.insert(0, int(self.first_number) * int(second_number))
        elif self.operation == "/":
            self.display.insert(0, int(self.first_number) / int(second_number))


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

