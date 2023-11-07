# Задание 1

n = int(input('Кол-во строк: '))
l = []

for i in range(n):
    l.append(int(input(f'Введите число {i+1}: ')))

l.reverse()

print(*l) 

# Задание 2

n = int(input('Кол-во строк: '))
l = []

for i in range(n):
    l.append(int(input(f'Введите число {i+1}: ')))

l.insert(0, l.pop())

print(*l)

# Задание 3

m = int(input('Максимальная масса: '))
n = int(input('Кол-во рыбаков: '))
l = []
count = 0

for i in range(n):
    l.append(int(input(f'Введите вес рыбака {i}: ')))

x = len(l)

for i in range(x):        
    if l != [] and len(l) != 1 and min(l) + max(l) <= m:
        count += 1
        l.pop((l.index(max(l))))
        l.pop((l.index(min(l))))
    elif l != []: 
        l.pop((l.index(max(l))))
        count += 1
    else:
        continue

print(count)
input()


  