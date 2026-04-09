import json
import csv
import pandas as pd

# Шляхи до файлів
input_json = "students.json"
output_json = "output.json"
input_csv = "students.csv"

# Дані
new_student = {"name": "Сергій", "age": 24, "faculty": "ФМ"}
search_name = "Олександра"
student_to_update = "Ольга"
new_faculty = "КН"
student_to_delete = "Наталія"

courses = [
    {"name": "Python програмування", "faculty": "КН", "credits": 5},
    {"name": "Бази даних", "faculty": "ІТ", "credits": 4},
    {"name": "Алгоритми", "faculty": "ФМ", "credits": 6}
]

# =========================
# JSON
# =========================
print("\n=== JSON ===")

# 1. Зчитування
with open(input_json, "r", encoding="utf-8") as f:
    students = json.load(f)

# 2. Вивід
print("Початкові дані:")
for s in students:
    print(s)

# 3. Додавання
students.append(new_student)

# 4. Пошук
print("\nПошук студента:")
found = False
for s in students:
    if s["name"] == search_name:
        print("Знайдено:", s)
        found = True
if not found:
    print("Студента не знайдено")

# 5. Оновлення
for s in students:
    if s["name"] == student_to_update:
        s["faculty"] = new_faculty

# 6. Видалення
students = [s for s in students if s["name"] != student_to_delete]

# 7. Додаємо курси
final_data = {
    "students": students,
    "courses": courses
}

# 8. Запис
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print("JSON файл оновлено (output.json)")


# =========================
# CSV
# =========================
print("\n=== CSV ===")

students_csv = []

# 1. Зчитування
with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        students_csv.append(row)

# 2. Вивід
print("Початкові CSV дані:")
for s in students_csv:
    print(s)

# 3. Додавання
students_csv.append(new_student)

# 4. Видалення
students_csv = [s for s in students_csv if s["name"] != student_to_delete]

# 5. Запис
with open("students_updated.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "faculty"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students_csv)

print("CSV файл оновлено (students_updated.csv)")


# =========================
# EXCEL
# =========================
print("\n=== EXCEL ===")

# 1. Зчитування
df = pd.read_excel("students.xlsx")

print("Початкові Excel дані:")
print(df)

# 2. Додавання
df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)

# 3. Фільтрація (вік > 19)
filtered_df = df[df["age"] > 19]

# 4. Сортування
sorted_df = filtered_df.sort_values(by="age")

# 5. Запис
sorted_df.to_excel("students_processed.xlsx", index=False)

print("Excel файл оброблено (students_processed.xlsx)")


# =========================
# CSV -> JSON
# =========================
print("\n=== CSV → JSON ===")

data = []

with open(input_csv, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["age"] = int(row["age"])
        data.append(row)

with open("converted.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Конвертацію завершено (converted.json)")