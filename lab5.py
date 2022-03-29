import math


def Triangle(a, b, c):
    if b < a > c:
        return a < b + c
    elif a < b > c:
        return b < a + c
    else:
        return c < a + b


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def number_to_words(n):
    dig = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    dec = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
           "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    teen = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать",
            "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    x = ""
    if n == 0:
        return "ноль"
    if 10 < n % 100 < 20:
        x += teen[n % 10]
    else:
        d = dec[n % 100 // 10]
        x += d + (d and " " or "") + dig[n % 10]
    return x


def power(a, n):
    step = 1
    for i in range(abs(n)):
        step *= a
    if n >= 0:
        return step
    else:
        return 1 / step


def powerrec(a, n):
    if n == 0:
        return 1
    res = powerrec(a * a, n // 2)
    if n % 2:
        res *= a
    return res


def palindrome(word):
    word = word.replace(' ', '').lower()
    if word == word[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


def mirror(arr):
    return arr + arr[::-1]


def print_without_duplicates(messages):
    i = 1
    print(messages[0])
    while i < len(messages):
        if messages[i] != messages[i - 1]:
            print(messages[i])
        i += 1


def print_without_duplicates(sms):
    if sms not in lst:
        print(sms)
        lst.append(sms)


def length(lst):
    if not lst:
        return 0
    return 1 + length(lst[1:])


lesson = int(input("Введите номер задания: "))

if lesson == 1:
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    print("Это треугольник" if Triangle(a, b, c) else "Это не треугольник")

elif lesson == 2:

    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))
    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))
    print(distance(x1, x2, y1, y2))

elif lesson == 3:
    print(number_to_words(int(input("Введите число: "))))

elif lesson == 4:
    print(power(float(input("Введите число а: ")), int(input("Введите число n: "))))

elif lesson == 5:
    print(palindrome(str(input("Введите строку: "))))

elif lesson == 6:
    lst = []
    lst1 = []
    print("Вводите сообщения, чтобы закончить ввод вместо ввода нового сообщения нажмите enter")
    word = str(input(""))
    while word != "":
        lst1.append(word)
        word = str(input(""))
    i = 0
    for i in range(len(lst1)):
        print_without_duplicates(lst1[i])

elif lesson == 7:
    print("я не понимаю как делать задание, слишком непонятный ввод данных")

elif lesson == 8:
    print("Введите числа через пробел: ")
    lst = [int(i) for i in input().split()]
    print(mirror(lst))

elif lesson == 9:
    print("то же что и в 7")

elif lesson == 13:
    print(powerrec(float(input("Введите число а: ")), int(input("Введите число n: "))))

elif lesson == 14:
    print("Введите числа через пробел: ")
    a = [int(i) for i in input().split()]
    print("Длина списка равна: ", length(a))
