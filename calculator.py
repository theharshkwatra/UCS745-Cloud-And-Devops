import tkinter as tk


def button_click(value):
    if value == "C":
        display.delete(0, tk.END)

    elif value == "=":
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    else:
        display.insert(tk.END, value)


root = tk.Tk()
root.title("Calculator - Versin B")
root.geometry("350x450")
root.resizable(False, False)

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)
display.pack(fill="x", padx=10, pady=20)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button in row:
        btn = tk.Button(
            frame,
            text=button,
            font=("Arial", 18),
            command=lambda value=button: button_click(value)
        )
        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)

root.mainloop()