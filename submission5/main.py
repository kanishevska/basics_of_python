# Дані для завдання

# Шлях до вхідного файлу
input_file = "input.txt"

# Шлях до вихідного файлу
output_file = "output.txt"

# Слово для пошуку (варіант 5)
word_to_find = "Python"

# Слово для заміни та нове слово (варіант 6)
word_to_replace = "World"
replacement_word = "Ukraine"

# Новий рядок для додавання (варіант 7)
new_line = "Новий рядок додано"

# Новий вміст для перезапису (варіант 10)
new_content = "Файл перезаписано"

# Реалізуйте завдання тут
import os

if not os.path.exists(input_file):
    print(f"Файл {input_file} не знайдено.")
else:
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Видаляємо тільки порожні рядки
    processed_lines = [line for line in lines if line.strip() != ""]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.writelines(processed_lines)

    print(f"Обробка завершена. Результат у файлі {output_file}.")