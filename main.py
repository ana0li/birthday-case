import datetime

# Словарь цифр для "табло"
digits = {
    '0': [" *** ",
          "*   *",
          "*   *",
          "*   *",
          " *** "],
    '1': ["  *  ",
          " **  ",
          "  *  ",
          "  *  ",
          " *** "],
    '2': [" *** ",
          "*   *",
          "   * ",
          "  *  ",
          "*****"],
    '3': [" *** ",
          "    *",
          " *** ",
          "    *",
          " *** "],
    '4': ["*   *",
          "*   *",
          "*****",
          "    *",
          "    *"],
    '5': ["*****",
          "*    ",
          "**** ",
          "    *",
          "**** "],
    '6': [" *** ",
          "*    ",
          "**** ",
          "*   *",
          " *** "],
    '7': ["*****",
          "    *",
          "   * ",
          "  *  ",
          " *   "],
    '8': [" *** ",
          "*   *",
          " *** ",
          "*   *",
          " *** "],
    '9': [" *** ",
          "*   *",
          " ****",
          "    *",
          " *** "],
    ' ': ["     ",
          "     ",
          "     ",
          "     ",
          "     "],
}

# Спрашиваем дату
day = int(input("Введи день рождения (число): "))
month = int(input("Введи месяц рождения (число): "))
year = int(input("Введи год рождения (четыре цифры): "))

# Создаём объект даты
birth_date = datetime.date(year, month, day)

# День недели
weekday = birth_date.strftime('%A')
weekdays_ru = {
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье"
}
print("📅 День недели:", weekdays_ru[weekday])

# Високосный?
is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
print("🚀 Високосный год?" , "Да" if is_leap else "Нет")

# Сколько лет
today = datetime.date.today()
age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
print("🎉 Тебе сейчас:", age, "лет")

# Печатаем дату как табло
date_str = birth_date.strftime("%d %m %Y")
print("\n✨ Дата на табло:\n")
for i in range(5):
    line = ""
    for char in date_str:
        line += digits[char][i] + "  "
    print(line)
