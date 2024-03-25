numbers = [int(s) for s in input('Введите последовательность чисел через пробел:').split()]
tmp = set()
for num in numbers:
    if num in tmp:
        print('YES')
    else:
        print('NO')
        tmp.add(num)