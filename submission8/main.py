# Лабораторна робота 8: Основи ООП

# Реалізуйте завдання тут
class CalendarEvent:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time

    def show_event(self):
        print(f"Подія: {self.title}")
        print(f"Дата: {self.date}")
        print(f"Час: {self.time}")

    def edit_event(self, new_title=None, new_date=None, new_time=None):
        if new_title:
            self.title = new_title
        if new_date:
            self.date = new_date
        if new_time:
            self.time = new_time


event1 = CalendarEvent("Зустріч", "10.04.2026", "14:00")

print("Початкові дані:")
event1.show_event()

event1.edit_event(new_title="Зустріч з викладачем", new_time="15:00")

print("Після редагування:")
event1.show_event()