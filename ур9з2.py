res1 = list(map(int, input('Введите числа через пробел:').split()))
res2 = list(map(int, input('Введите числа через пробел:').split()))
c = []
for i in res1:
    if i in res2 and i not in c:
        c.append(i)       
print('Количество пересечений чисел:', len(c))
