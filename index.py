import tkinter as tk
def calculate(divisor):
    try:
        value = float(entry.get())
        result = value / divisor
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# GUI Window
root = tk.Tk()
root.title("Three Calculations")
root.geometry("300x250")

# Input field
entry_label = tk.Label(root, text="Enter a value:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Buttons for each condition
btn1 = tk.Button(root, text="Divide by 9", command=lambda: calculate(1.18))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Divide by 6", command=lambda: calculate(1.12))
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Divide by 5", command=lambda: calculate(1.15))
btn3.pack(pady=5)

# Result display
result_label = tk.Label(root, text="Result:")
result_label.pack(pady=10)

# Run the application
root.mainloop()