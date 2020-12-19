import random


# проверка, что введенное это цифры
def is_valid(num):
    if num.isdecimal() and 1 <= int(num) <= 100:
        return True
    else:
        return False


def guess_the_number():
    n = random.randint(1, 100)
    print('Добро пожаловать в числовую угадайку!')
    print('Попробуйте угадать число от 1 до 100')
    print(n)
    counter = 0
    for i in range(100):
        user_variant = input()
        if is_valid(user_variant):
            if int(user_variant) < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
                continue
            elif int(user_variant) > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
                continue
            elif int(user_variant) == n:
                counter += 1
                print('Вы угадали c', counter, 'попытки! поздравляем!')
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue


print(guess_the_number())
