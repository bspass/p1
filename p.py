import tkinter as tk
import random
import string

def generate_password():

    password_length = random.randrange(1, 16)

    password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Генератор паролей")

generate_button = tk.Button(root, text="Генерировать", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

password_label = tk.Label(root, text="Сгенерированный пароль:")
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
