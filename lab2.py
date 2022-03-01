lesson = int(input("введите номер задания: "))
if lesson == 1:
    word = input("Введите слово: ")
    print(word[2])
    print(word[-2])
    print(word[:5])
    print(word[:-2])
    print(word[::2])
    print(word[1::2])
    print(word[::-1])
    print(word[::-2])
    print(len(word))

elif lesson == 2:
    word = input("Введите слово: ")
    print(word[(len(word) + 1) // 2:] + word[:(len(word) + 1) // 2])

elif lesson == 3:
    word = input("Введите слово: ")
    before_h = word.find('h')
    after_h = word.rfind('h')
    print(word[:before_h] + word[after_h:before_h:-1] + word[after_h:])

elif lesson == 4:
    word = input("Введите слово: ")
    if word.count('f') == 1:
        print(word.find('f'))
    elif word.count('f') >= 2:
        print(word.find('f'), word.rfind('f'))

elif lesson == 5:
    print("Введите числа через пробел: ")
    lst = [int(i) for i in input().split()]
    i = 1
    while i < len(lst):
        if lst[i] > lst[i - 1]:
            print(lst[i])
        i += 1

elif lesson == 6:
    print("Введите числа через пробел: ")
    lst = [int(i) for i in input().split()]
    i = 1
    while i < len(lst):
        if lst[i - 1] * lst[i] > 0:
            print(lst[i - 1], lst[i])
            break
        i += 1

elif lesson == 7:
    print("Введите числа через пробел: ")
    lst = [int(i) for i in input().split()]
    for i in range(1, len(lst), 2):
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
    print(' '.join([str(i) for i in lst]))

elif lesson == 8:
    print("Введите числа через пробел: ")
    lst = [int(s) for s in input().split()]
    for i in range(0, len(lst)):
        if lst.count(lst[i]) == 1:
            print(lst[i], end=' ')