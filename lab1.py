lesson = int(input("введите номер задания: "))
if lesson == 1:
    kino = [input("Введите название фильма: "),
            input("Введите название кинотеатра: "),
            input("Введите время сеанса: ")]
    print("Билет на ", kino[0], " в ", kino[1], " на ", kino[2],
          " забронирован.")

elif lesson == 2:
    whatsif = [input("Введите 1 слово: "), input("Введите 2 слово: ")]
    if whatsif[0] == whatsif[0] == ("да" or "нет"):
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")

elif lesson == 3:
    n3 = [input("Введите логин: "), input("Введите резервный адрес: ")]
    if "@" in n3[0]:
        print("логин не должен содержать @")
    elif not ("@" in n3[1]):
        print("резервный адрес должен содержать @")
    else:
        print("все введено верно")

elif lesson == 4:
    print(input())

elif lesson == 5:
    n5 = input()
    if n5 == "":
        print("YES")
    else:
        print("NO")

elif lesson == 6:
    n6 = int(input("Введите число: "))
    if (n6 % 10 + n6 // 100) / 2 == n6 // 10 % 10:
        print("Вы ввели красивое число")
    else:
        print("Жаль, вы ввели обычное число")

elif lesson == 7:
    num = int(input())
    a = num % 10
    num //= 10
    b = num % 10
    num //= 10
    c = num % 10
    d = num // 10
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if c > d:
        c, d = d, c
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    if a == 0 and b:
        a, b = b, a
    elif a == 0 and c:
        a, c = c, a
    elif a == 0 and d:
        a, d = d, a
    print(d + 10 * (c + 10 * (b + 10 * a)))


elif lesson == 8:
    rost = input("Введите рост претендента: ")
    if rost != "!":
        max_rost = 150
        min_rost = 190
    kol = 0
    while rost != "!":
        rost = int(rost)
        if 150 < rost < 190:
            kol += 1
            if min_rost > rost:
                min_rost = rost
            elif max_rost < rost:
                max_rost = rost
        rost = input("Введите рост претендента: ")
    print(kol)
    print(min_rost, " ", max_rost)

elif lesson == 9:
    while True:
        password = input("введите пароль: ")
        password1 = input("повторите ввод пароля: ")
        if len(password) < 8:
            print("Короткий!")
            print("Повтроите ввод")
            continue
        elif password != password1:
            print("НЕ совпадают пароли!")
            print("Повтроите ввод")
            continue
        elif "123" in password:
            print("простой!")
            print("Повтроите ввод")
            continue
        else:
            break
    print("OK!")

elif lesson == 10:
    stop = ""
    fact = 1
    lst=[]
    while stop != "x":
        num = int(input())
        stop = input()
        if stop == "x":
            lst.append(num)
            break
        else:
            if stop == '+':
                num1 = int(input())
                lst.append(num+num1)
            elif stop == '-':
                num1 = int(input())
                lst.append(num-num1)
            elif stop == '*':
                num1 = int(input())
                lst.append(num*num1)
            elif stop == '/':
                num1 = int(input())
                if num1 == 0:
                    continue
                else:
                    lst.append(num//num1)
            elif stop == '!' and num > 0:
                for i in range(1, num + 1):
                    fact *= i
                lst.append(fact)
            elif num == 0 and stop == '!':
                lst.append("1")
            elif stop == '%':
                num1 = int(input())
                if num1 == 0:
                    continue
                else:
                    lst.append(num%num1)
    for i in range(0,len(lst)):
        print(lst[i])

elif lesson == 11:
    ray = int(input("введите колличество рядов: ")) - 1
    zvezd = 1
    while ray > -1:
        print(' ' * ray + '*' * zvezd)
        zvezd += 2
        ray -= 1

elif lesson == 12:
    num = [str(i) for i in range(1, int(input('Введите число: ')) + 1)]
    a = 0
    while num:
        print(' '.join(num[:a + 1]))
        a += 1
        num = num[a:]

elif lesson == 13:
    hight = int(input("Введите высоту: "))
    wight = int(input("Введите ширину: "))
    str = input()
    for i in range(hight):
        if i == 0 or i == hight - 1:
            for j in range(wight):
                print(str, end='')
        else:
            print(str, end='')
            for j in range(1, wight - 1):
                print(' ', end='')
            print(str, end='')
        print()