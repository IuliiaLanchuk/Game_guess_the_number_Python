import random
from tkinter import *


# кнопка Начать игру
def clicked():
    lbl.configure(text="Добро пожаловать в числовую угадайку!\n\nЯ уже загадала число от 1 до 100.\n\n"
                       "Попробуй угадать число.", padx="50", pady="8")
    btn_start.destroy()
    variant.grid(column=0, row=3)
    btn_guess.grid(column=0, row=4, padx="20", pady="8.5")


# кнопка Угадать
def guessed():
    value = variant.get()
    if value:
        print(value)
    else:
        print('Empty Entry')
    print('кнопка угадать нажата')  # это выведется в консоли
    if is_valid(value):
        if int(value) < n:
            lbl.configure(text="Ваше число меньше загаданного,\n попробуйте еще разок", padx="60", pady="18")
        elif int(value) > n:
            lbl.configure(text="Ваше число больше загаданного,\n попробуйте еще разок", padx="60", pady="18")
        elif int(value) == n:
            variant.destroy()
            btn_guess.destroy()
            lbl.configure(text='Вы угадали! Поздравляем!\n\nСпасибо, что играли в числовую угадайку.\nЕще увидимся...')
    else:
        lbl.configure(text='А может быть все-таки введем\n целое число от 1 до 100?', padx="80", pady="8")
        print('А может быть все-таки введем целое число от 1 до 100?')


# проверка, что введенное это цифры
def is_valid(num):
    if num.isdecimal() and 1 <= int(num) <= 100:
        return True
    else:
        return False


window = Tk()
window.title("Приложение Угадайка")
window.config(bg='LightSteelBlue3')
window.geometry('350x250')
lbl = Label(window, text="Привет,меня зовут Юля!\nСыграешь со мной в угадайку? Тогда жми на кнопку!",
            font=("Arial", 10), bg='LightSteelBlue3', padx="10", pady="18")
lbl.grid(column=0, row=0)
btn_start = Button(window, text="Начать игру", bg="gray", fg="grey26", command=clicked)
btn_start.grid(column=0, row=1)
btn_guess = Button(window, text="Угадать", bg="gray", fg="grey26", command=guessed)
variant = Entry(window)
# здесь генерируется случайное число
n = random.randint(1, 100)
# в консоль выведется загаданное число
print('Рандом-', n)
window.mainloop()
