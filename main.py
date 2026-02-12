import math  # Included for scope of `eval()` function.
import tkinter as tk
from functools import partial
from tkinter import ttk

# NOTE: LSP code rules:
# - ty LSP can perform type checking if you use hinting.
#      Always use hinting on variables.
# - Ruff LSP doesn't support star imports. Don't use star imports.
# INFO: Curricular competencies met:
# - Nothing yet!

# ------- Functions

# ----- Calculate functions


# Defined to be accurate based on en.wikipedia.org/wiki/Factorial
# Since negative factorials are not possible, -1 is returned in those
#   cases to indicate an error.
def factorial(n: int) -> int:
    # If n is negative, return -1 to indicate error.
    if n < 0:
        return -1
    # If n is 0 or 1, return 1, as that is correct in that case.
    if n == 0 or n == 1:
        return 1

    # Calculate factorial using recursion
    factorial: int = 1

    for i in range(2, n + 1):
        factorial *= i

    return factorial


# ----- Event functions


# Enters a string into the expression box; used for buttons.
def enterText(char: str) -> None:
    oldExpression: str = expression.get()
    expression.set(oldExpression + char)


# Calculates the result and packs it into the output label.
def calculate() -> None:
    output.set(eval(expression.get()))


# ------- Initialization

# ----- Initialize Tk and window
# Initialize Tk instance and window
root: tk.Tk = tk.Tk()
root.title("Calculator")

# Initialize themed frame
main_frame: ttk.Frame = ttk.Frame(root, padding=(12, 12, 12, 12))
main_frame.grid(sticky="nsew")

# Ensure main_frame expands to window size
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# ----- Define layout and widgets
# --- Expression view/entry
expression: tk.StringVar = tk.StringVar()
expression_entry: ttk.Entry = ttk.Entry(main_frame, textvariable=expression)
expression_entry.grid(sticky="new")

# --- Output pane
output: tk.StringVar = tk.StringVar(value="= ?")
output_label: ttk.Label = ttk.Label(
    main_frame, anchor="e", textvariable=output
)
output_label.grid(row=1, sticky="ew")

# --- Buttons panes
# Create buttons notebook (creates tabs for switching between button sets)
buttons_notebook: ttk.Notebook = ttk.Notebook(main_frame)
buttons_notebook.grid(row=2, sticky="nsew")

# Let buttons notebook take additional space
main_frame.rowconfigure(2, weight=1)
main_frame.columnconfigure(0, weight=1)

# Add arithmetic buttons frame
arithmetic_frame: ttk.Frame = ttk.Frame()
buttons_notebook.add(arithmetic_frame, text="Common")

# --- Buttons

# -- Arithmetic frame

# - Buttons definitions

button_1: ttk.Button = ttk.Button(
    arithmetic_frame, text="1", command=partial(enterText, "1")
)
button_2: ttk.Button = ttk.Button(
    arithmetic_frame, text="2", command=partial(enterText, "2")
)
button_3: ttk.Button = ttk.Button(
    arithmetic_frame, text="3", command=partial(enterText, "3")
)
button_4: ttk.Button = ttk.Button(
    arithmetic_frame, text="4", command=partial(enterText, "4")
)
button_5: ttk.Button = ttk.Button(
    arithmetic_frame, text="5", command=partial(enterText, "5")
)
button_6: ttk.Button = ttk.Button(
    arithmetic_frame, text="6", command=partial(enterText, "6")
)
button_7: ttk.Button = ttk.Button(
    arithmetic_frame, text="7", command=partial(enterText, "7")
)
button_8: ttk.Button = ttk.Button(
    arithmetic_frame, text="8", command=partial(enterText, "8")
)
button_9: ttk.Button = ttk.Button(
    arithmetic_frame, text="9", command=partial(enterText, "9")
)
button_0: ttk.Button = ttk.Button(
    arithmetic_frame, text="0", command=partial(enterText, "0")
)

button_decimal: ttk.Button = ttk.Button(
    arithmetic_frame, text=".", command=partial(enterText, ".")
)

button_divide: ttk.Button = ttk.Button(
    arithmetic_frame, text="/", command=partial(enterText, "/")
)
button_multiply: ttk.Button = ttk.Button(
    arithmetic_frame, text="*", command=partial(enterText, "*")
)
button_subtract: ttk.Button = ttk.Button(
    arithmetic_frame, text="-", command=partial(enterText, "-")
)
button_add: ttk.Button = ttk.Button(
    arithmetic_frame, text="+", command=partial(enterText, "+")
)

button_equals: ttk.Button = ttk.Button(
    arithmetic_frame, text="=", command=calculate
)

# - Button layout

button_7.grid(row=1, column=1, sticky="nsew")
button_8.grid(row=1, column=2, sticky="nsew")
button_9.grid(row=1, column=3, sticky="nsew")
button_divide.grid(row=1, column=4, sticky="nsew")
button_4.grid(row=2, column=1, sticky="nsew")
button_5.grid(row=2, column=2, sticky="nsew")
button_6.grid(row=2, column=3, sticky="nsew")
button_multiply.grid(row=2, column=4, sticky="nsew")
button_1.grid(row=3, column=1, sticky="nsew")
button_2.grid(row=3, column=2, sticky="nsew")
button_3.grid(row=3, column=3, sticky="nsew")
button_subtract.grid(row=3, column=4, sticky="nsew")
button_0.grid(row=4, column=1, sticky="nsew")
button_decimal.grid(row=4, column=2, sticky="nsew")
button_equals.grid(row=4, column=3, sticky="nsew")
button_add.grid(row=4, column=4, sticky="nsew")

arithmetic_frame.columnconfigure(0, weight=1)
arithmetic_frame.rowconfigure(0, weight=1)

# --- Finalizing

#

# --- Start main loop
root.mainloop()
