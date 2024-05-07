import tkinter as tk  # Импортируем модуль tkinter, который используется для создания графического интерфейса.
import random  # Импортируем модуль random, который используется для случайных генераций.
import string  # Импортируем модуль string, который содержит в себе буквы, цифры и спец. символы.


def generate_password():  # Определяем функцию для генерации пароля.
    # Получаем длину пароля из поля ввода, преобразуя ввод в целое число.
    password_length = int(length_entry.get())
    # Инициализируем пустую строку для возможных символов пароля.
    password_characters = ""

    if include_lowercase.get():
        password_characters += string.ascii_lowercase
    if include_uppercase.get():
        password_characters += string.ascii_uppercase
    if include_digits.get():
        password_characters += string.digits
    if include_special.get():
        password_characters += string.punctuation

    # Генерируем пароль заданной длины, используя случайные символы из выбранных типов.
    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    # Очищаем поле для отображения пароля и вставляем сгенерированный пароль.
    password_entry.delete(0, tk.END)  # Удаляем все символы в поле.
    password_entry.insert(0, password)  # Вставляем новый пароль.


# Создаем главное окно приложения.
root = tk.Tk()
root.title("Генератор паролей")  # Устанавливаем заголовок окна.

# Создаем элементы интерфейса для ввода данных и отображения результатов.
# Метка и поле ввода для длины пароля.
length_label = tk.Label(root, text="Длина пароля:")  # Метка с текстом.
length_label.grid(row=0, column=0, padx=10, pady=10)  # Размещаем метку в сетке с отступами.
length_entry = tk.Entry(root)  # Поле ввода для длины пароля.
length_entry.grid(row=0, column=1, padx=10, pady=10)  # Размещаем поле для ввода длины строки.

include_lowercase = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(root, text="Прописные буквы", variable=include_lowercase)
lowercase_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

include_uppercase = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Заглавные буквы", variable=include_uppercase)
uppercase_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

include_digits = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Цифры", variable=include_digits)
digits_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

include_special = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Спец. символы", variable=include_special)
special_checkbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Создаем кнопку для запуска функции генерации пароля.
generate_button = tk.Button(root, text="Генерировать", command=generate_password)  # Кнопка запуска генерации пароля.
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)  # Размещаем кнопку в сетке.

# Метка для отображения сгенерированного пароля.
password_label = tk.Label(root, text="Сгенерированный пароль:")  # Метка с текстом для результата.
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)  # Размещаем метку в сетке.

# Поле для отображения сгенерированного пароля.
password_entry = tk.Entry(root, width=30)  # Поле ввода/вывода для пароля.
password_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5)  # Размещаем в сетке.

# Запуск основного цикла программы, который обрабатывает события интерфейса.
root.mainloop()  # Начинаем основной цикл приложения, который удерживает окно открытым для взаимодействия с элементами
