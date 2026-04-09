# Дані для завдання

# Словник для перевірки (варіант 6)
data = {"name": "Олена", "age": 20, "faculty": "КН"}

# Файл для запису помилок (варіант 8)
error_file = "error.log"

# Файл для зчитування (варіанти 5, 9)
input_file = "input.txt"

# Формат даних у файлі (варіант 9): "ім'я:вік" у кожному рядку

# Реалізуйте завдання тут
def log_error(message):
    """Запис помилки у файл та вивід на екран"""
    print(message)
    with open(error_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")

try:
    # Відкриваємо файл для зчитування
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("Зчитані дані з файлу:")
    for line in lines:
        line = line.strip()
        try:
            # Перевірка формату "ім'я:вік"
            if ":" not in line:
                raise ValueError(f"Неправильний формат рядка: '{line}'")
            name, age = line.split(":", 1)
            age = int(age)  # перевірка, що вік — число
            print(f"Ім'я: {name}, Вік: {age}")
        except ValueError as ve:
            log_error(f"Помилка обробки рядка: {ve}")

except FileNotFoundError:
    log_error(f"Помилка: файл '{input_file}' не знайдено.")
except Exception as e:
    log_error(f"Непередбачена помилка: {e}")
finally:
    print("Програма завершила виконання.")