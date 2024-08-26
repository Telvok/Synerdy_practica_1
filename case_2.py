from datetime import datetime

def user_birthday():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return datetime(year, month, day)

def day_of_week(birthday):
    return birthday.strftime("%A")

def long_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def age(birthday):
    today = datetime.now()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def tablo(birthday):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", "  *  ", "  *  ", "*****"],
        '2': [" *** ", "*   *", "    *", "   * ", "  *  ", " *   ", "*****"],
        '3': ["*****", "    *", "  *  ", "   * ", "    *", "*   *", " *** "],
        '4': ["   * ", "  ** ", " * * ", "*  * ", "*****", "   * ", "   * "],
        '5': ["*****", "*    ", "**** ", "    *", "    *", "*   *", " *** "],
        '6': [" *** ", "*   *", "*    ", "**** ", "*   *", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", "  *  ", "  *  ", "  *  "],
        '8': [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "],
        '9': [" *** ", "*   *", "*   *", " ****", "    *", "   * ", " **  "],
        '-': ["     ", "     ", "     ", "     ", "     ", "     ", "     "]    
    }
    for i in range(7):
        line = ""
        for char in birthday:
            line += digits[char][i] + "  "
        print(line)

birthday = user_birthday()
print("День недели:", day_of_week(birthday))
print("Високосный год:", long_year(birthday.year))
print("Возраст:", age(birthday))
tablo(birthday.strftime("%d-%m-%Y"))