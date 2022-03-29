lesson = int(input("Введите номер задания: "))


def factorials(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x


def square_fibonacci(n):
    first = 1
    second = 0
    for _ in range(n):
        first, second = second, first + second
        yield second ** 2


def alphabet():
    i = ord('А') - 1
    while i != ord('Я'):
        i += 1
        yield chr(i)


def arithmetic_operation(operation):
    if operation == '+':
        return lambda a, b: a + b
    elif operation == '-':
        return lambda a, b: a - b
    elif operation == '*':
        return lambda a, b: a * b
    elif operation == '/':
        return lambda a, b: a / b


def same_by(characteristics, objects):
    for i in objects:
        if characteristics(i):
            return False

    return True


def print_operation_table(operation, table_rows=9, table_column=9):
    for i in range(1, table_column + 1):
        for j in range(1, table_rows + 1):
            if i == 1:
                print(j, end="\t")
            else:
                if j == 1:
                    print(i, end="\t")
                else:
                    print(operation(i, j), end="\t")
        print()


def check_password(func):
    flag = True

    def wrapper(n):
        nonlocal flag
        if flag:
            if input('Пароль: ') != '123':
                print("В доступе отказано")
                return None
            else:
                flag = False
                return func(n)

    return wrapper


@check_password
def fibonacci(n):
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    return f2


if lesson == 1:
    lst = [1, 2, 3, 4, 5, 6]
    print(list(filter(lambda x: x < 5, lst)))
    print(list(x for x in lst if x < 5))

elif lesson == 2:
    lst = [1, 2, 3, 4, 5, 6]
    print(list(map(lambda x: x / 2, lst)))
    print(list(x / 2 for x in lst))

elif lesson == 3:
    print(sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0,
                                           list(i for i in range(1, 101))))))

elif lesson == 4:
    lst = list(i for i in range(10, 21))
    print(list(map(lambda x: x / 2, filter(lambda x: x > 17, lst))))
    print(list(x / 2 for x in lst if x > 17))

elif lesson == 5:
    print(list(factorials(7)))

elif lesson == 6:
    print(list(square_fibonacci(7)))

elif lesson == 7:
    print(list(alphabet()))

elif lesson == 8:
    generator = (chr(i) for i in range(ord('А'), ord('Я') + 1))
    print(list(generator))

elif lesson == 9:
    operation = arithmetic_operation('+')
    print(operation(1, 4))

elif lesson == 10:
    values = [0, 2, 10, 6]
    if same_by(lambda x: x % 2, values):
        print('same')
    else:
        print('different')

elif lesson == 11:
    print_operation_table(lambda x, y: x + y, 5, 5)

elif lesson == 12:
    words = input()
    res = sorted(words.split(), key=str.lower)
    print(' '.join(res))

elif lesson == 13:
    words = input()
    res = map(int, sorted(words.split()))
    res = sorted(res, key=abs)

    print(' '.join(map(str, res)))

elif lesson == 14:
    lst = [[23, 5], [0, 1], [1, 0], [3, 6], [6, 7], [2, -1], [2, 1]]
    lst.sort(key=lambda lst: (lst[0] ** 2 + lst[1] ** 2) ** 0.5)
    print(*lst)

elif lesson == 15:
    print('True') if (any(int(number) == 0 for number in list(input().split()))) else print('False')

elif lesson == 18:
    print(fibonacci(10))
