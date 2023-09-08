# 4. Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#
# from random import
# randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_TRIES = 10

number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Добро пожаловать в игру 'Угадай число'!")
print(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}.")

for tries in range(1, MAX_TRIES + 1):
    guess = int(input(f"Попытка {tries}: Ваш вариант: "))

    if guess < number:
        print("Загаданное число больше.")
    elif guess > number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляем! Вы угадали число {number} за {tries} попыток.")
        break
else:
    print(f"Игра окончена. Загаданное число: {number}")
