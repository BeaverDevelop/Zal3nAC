# Библиотеки
import keyboard
import mouse
import time
import locale
import os


# Перевод
def translate(text, lang="en"):
    if lang == "en":
        return text
    elif lang == "ru":
        if text == "Start":
            return "Запустить"
        elif text == "Zal3n AC":
            return "Zal3n AC"
        elif text == "What key do you want to use to activate it?\n":
            return "Какую клавишу для активации вы хотите использовать?\n"
        elif text == "Which mouse button should you click?\nLeft - 1\nRight - 2\n":
            return "На какую кнопку мыши нужно нажимать?\nЛевая - 1\nПравая - 2\n"
        elif text == "Error":
            return "Ошибка"
        elif text == "Settings saved!\nTo start, press {hot_key}":
            return f"Настройки сохранены!\nДля запуска нажмите {hot_key}"
        elif text == "Clicker deactivated":
            return "Кликер деактивирован"
        elif text == "Clicker activated":
            return "Кликер активирован"
    else:
        return text


# Очистка консоли
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# Выбор языка
print(translate("Start", locale.getdefaultlocale()[0]))
lang = input("Choose language: (ru/en)\n")
if lang.lower() not in ["ru", "en"]:
    print(translate("Error"))
    exit()

# Очищаем консоль перед заставкой
clear_console()

# Заставка
print(translate("Zal3n AC", lang))
time.sleep(3)

# Статус автокликера
Status = False

# Сохранение настроек автокликера
hot_key = input(translate("What key do you want to use to activate it?\n", lang))
mouse_selector = input(
    translate("Which mouse button should you click?\nLeft - 1\nRight - 2\n", lang)
)

if mouse_selector == "1":
    mouse_selector = "left"

elif mouse_selector == "2":
    mouse_selector = "right"

else:
    print(translate("Error", lang))
    exit()

# Вывод сообщения о сохранении настроек
if lang == "ru":
    print(f"Настройки сохранены!\nДля запуска нажмите {hot_key}")
else:
    print(translate(f"Settings saved!\nTo start, press {hot_key}", lang))


# Обработчик кликера
def clicker():
    global Status
    if Status:
        Status = False
        print(translate("Clicker deactivated", lang))
    else:
        Status = True
        print(translate("Clicker activated", lang))


keyboard.add_hotkey(hot_key, clicker)

while True:
    if Status:
        mouse.double_click(button=mouse_selector)
        time.sleep(0.01)