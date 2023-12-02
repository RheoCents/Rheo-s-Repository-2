import tkinter as tk
from tkinter import messagebox

def open_main_window():
    user_name = name_entry.get
    user_age = age_entry.get
    user_address = address_entry.get

    if user_name.strip() and user_age.strip() and user_address.strip():
        if 16 <= int(user_age) <= 70:
            top.destroy()
            root.deiconify()
        else:
            messagebox.showerror("Error", "Age must be between 16 and 70.")
    else:
        messagebox.showerror("Error", "Please fill in all the fields.")

def calculate_total():
    try:
        apples_entry_value = apples_entry.get
        oranges_entry_value = oranges_entry.get

        apples_quantity = int(apples_entry_value) if apples_entry_value else 0
        oranges_quantity = int(oranges_entry_value) if oranges_entry_value else 0

        if apples_quantity > 1000 and oranges_quantity > 1000:
            total_label.config(text=" You cannot go over 1000 oranges and apples",
                               foreground="red")
            price_label.config(text="")

        elif apples_quantity < 0 and oranges_quantity < 0:
            total_label.config(text="You can't buy negative apples and oranges.", foreground="red")
            price_label.config(text="")

        elif apples_quantity < 0:
            total_label.config(text="You can't buy negative apples.", foreground="red")
            price_label.config(text="")

        elif oranges_quantity < 0:
            total_label.config(text="You can't buy negative oranges.", foreground="red")
            price_label.config(text="")

        elif apples_quantity > 1000:
            total_label.config(text=" You cannot go over 1000 apples",
                               foreground="red")
            price_label.config(text="")

        elif oranges_quantity > 1000:
            total_label.config(text=" You cannot go over 1000 oranges",
                               foreground="red")
            price_label.config(text="")

        elif apples_quantity in range(0, 1000):
            apple_price = 20
            orange_price = 25

            total_amount = (apples_quantity * apple_price) + (oranges_quantity * orange_price)
            apple_price_total = apples_quantity * apple_price
            orange_price_total = oranges_quantity * orange_price

            total_label.config(text=f"\nTotal amount to pay: {total_amount} pesos\n", foreground="#b48cff")
            price_label.config(
                text=f"Apple's total price: {apple_price_total} pesos\nOrange's total price: {orange_price_total} pesos",
                foreground="#09ff00", background="black")
        elif oranges_quantity in range(-1, 1000):
            apple_price = 20
            orange_price = 25

            total_amount = (apples_quantity * apple_price) + (oranges_quantity * orange_price)
            apple_price_total = apples_quantity * apple_price
            orange_price_total = oranges_quantity * orange_price

            total_label.config(text=f"\nTotal amount to pay: {total_amount} pesos\n", foreground="#b48cff")
            price_label.config(
                text=f"Apple's total price: {apple_price_total} pesos\nOrange's total price: {orange_price_total} pesos",
                foreground="#09ff00", background="black")

    except ValueError:
        total_label.config(text="You cannot enter letters silly", foreground="RED", background="black")
        price_label.config(text="")

def open_input_window():
    global top
    top = tk.Toplevel()
    top.title("Welcome to Rheo's Shop")
    top.config(background="black")
    top.geometry("600x230")

    global name_entry, age_entry, address_entry
    tk.Label(top, text="Come on in, we sell apple and oranges \nTo initiate the transaction we first need your age, "
                       "name, and address \n This is so that we will know who our customer is\n",
             background="black", foreground= "Orange" ).pack()
    global name_entry, age_entry, address_entry

    tk.Label(top, text="Name:", background="black", foreground="#00eaff").pack()
    name_entry = tk.Entry(top)
    name_entry.pack()

    tk.Label(top, text="Age:", background="black", foreground="#00eaff").pack()
    age_entry = tk.Entry(top)
    age_entry.pack()

    tk.Label(top, text="Address:", background="black", foreground="#00eaff").pack()
    address_entry = tk.Entry(top)
    address_entry.pack()

    submit_button = tk.Button(top, text="Submit", command=open_main_window, foreground="white", background="black")
    submit_button.pack()

def confirm_order():
    confirmation_message = f"Your order has been confirmed!"
    messagebox.showinfo("Order Confirmed", confirmation_message)

root = tk.Tk()
root.title("Rheo's Shop")
root.configure(background="black")
root.geometry("400x230")

open_input_window()

apples_label = tk.Label(root, text="Enter number of apples:", foreground="#00eaff", background="black")
apples_label.pack()

apples_entry = tk.Entry(root)
apples_entry.pack()

oranges_label = tk.Label(root, text="Enter number of oranges:", foreground="#00eaff", background="black")
oranges_label.pack()

oranges_entry = tk.Entry(root)
oranges_entry.pack()

calculate_button = tk.Button(root, text="Calculate", foreground="White", background="black", command=calculate_total)
calculate_button.pack()

total_label = tk.Label(root, text="Orange's price = 25 pesos\nApple's price = 20 pesos", foreground="Orange",
                       background="black")
total_label.pack()

order_button = tk.Button(root, text="Order",command=confirm_order,foreground="White",
                       background="black")
order_button.pack()

price_label = tk.Label(root, text="", foreground="Orange", background="black")
price_label.pack()

root.withdraw()
root.mainloop()
