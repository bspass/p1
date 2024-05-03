import tkinter as tk    # Импортируем модуль tkinter, который используется для создания графического интерфейса.
import random   # Импортируем модуль random, который используется для случайных генераций.
import string   # Импортируем модуль string, который содержит в себе буквы, цифры и спец. символы.


def generate_password():    # Определяем функцию для генерации пароля.
    # Получаем длину пароля из поля ввода, преобразуя ввод в целое число.
    password_length = random.randrange(1, 16)
    # Инициализируем пустую строку для возможных символов пароля.
    password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # Генерируем пароль заданной длины, используя случайные символы из выбранных типов.
    password = ''.join(random.choice(password_characters) for _ in range(password_length))

    # Очищаем поле для отображения пароля и вставляем сгенерированный пароль.
    password_entry.delete(0, tk.END)    # Удаляем все символы в поле.
    password_entry.insert(0, password)  # Вставляем новый пароль.


# Создаем главное окно приложения.
root = tk.Tk()
root.title("Генератор паролей")  # Устанавливаем заголовок окна

# Создаем кнопку для запуска функции генерации пароля.
length_label = tk.Label(root, text="Длина пароля:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button = tk.Button(root, text="Генерировать", command=generate_password)   # Кнопка запуска генерации пароля.
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)   # Размещаем кнопку в сетке.

# Метка для отображения сгенерированного пароля.
password_label = tk.Label(root, text="Сгенерированный пароль:")     # Метка с текстом для результата.
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)     # Размещаем метку в сетке.

# Поле для отображения сгенерированного пароля.
password_entry = tk.Entry(root, width=30)   # Поле ввода/вывода для пароля.
password_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=5)     # Размещаем в сетке.

# Запуск основного цикла программы, который обрабатывает события интерфейса.
root.mainloop()  # Начинаем основной цикл, который удерживает окно открытым для взаимодействия с элементами интерфейса.
