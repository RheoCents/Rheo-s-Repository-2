import tkinter as tk
from tkinter import messagebox

def calculate_max_apples():
    try:
        money_amount = float(money_var.get())
        apple_price = float(price_var.get())

        if money_amount >= 0 and apple_price >= 0:
            max_apples = int(money_amount // apple_price)
            remaining_money = money_amount % apple_price

            result_label.config(text=f"Maximum apples you can buy: {max_apples}\nRemaining money: {remaining_money:.2f} pesos")
        else:
            messagebox.showerror("Error", "You can't enter negative numbers you silly")
    except ValueError:
        messagebox.showerror("Error", "You can't enter letters you know")

root = tk.Tk()
root.title("Rheo's Apples Calculator")
root.geometry("350x200")
root.configure(background="Black")

money_label = tk.Label(root, text="Enter the amount of money you have:", foreground="#00eaff", background="black")
money_label.pack()

money_var = tk.StringVar()
money_entry = tk.Entry(root, textvariable=money_var)
money_entry.pack()

price_label = tk.Label(root, text="Enter the price of an apple:", foreground="#00eaff", background="black")
price_label.pack()

price_var = tk.StringVar()
price_entry = tk.Entry(root, textvariable=price_var)
price_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_max_apples, foreground="White", background="black")
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="This is to help you \nfind out how many apples "
                                   "\nyou can buy with you money", foreground="Orange",
                       background="black")
result_label.pack()

root.mainloop()
