"""Modules Used In This Program"""
import tkinter as tk
import secrets
import string


def generate_password(
    length=14, use_uppercase=True, use_digits=True, use_punctuation=True
):
    """Generate a secure, random password."""
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    secure_password = "".join(secrets.choice(characters) for i in range(length))
    return secure_password


def generate_and_display_password():
    """Generate a password using the specified options and display it in the GUI."""
    try:
        length = int(length_entry.get())
        if length < 8 or length > 24:
            password_label.config(text="Length must be between 8 and 24")
            return
    except ValueError:
        password_label.config(text="Please enter a valid number")
        return
    password = generate_password(
        length, uppercase_var.get(), digits_var.get(), punctuation_var.get()
    )
    password_label.config(text=password)


def copy_to_clipboard():
    """Copy the displayed password to the system clipboard."""
    password = password_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(password)


root = tk.Tk()
root.title("Secure Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(
    root, text="Include Uppercase Letters", variable=uppercase_var
)
uppercase_check.pack()

digits_var = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

punctuation_var = tk.BooleanVar(value=True)
punctuation_check = tk.Checkbutton(
    root, text="Include Punctuation", variable=punctuation_var
)
punctuation_check.pack()

generate_button = tk.Button(
    root, text="Generate Password", command=generate_and_display_password
)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Update idletasks to get updated window size
root.update_idletasks()

# Get the window size
window_width = root.winfo_width()
window_height = root.winfo_height()

# Calculate position for centering the window
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)

# Set the window's position
root.geometry(f"+{position_right}+{position_down}")

root.mainloop()
