print() # Команда вывода на экран

print(3 + 4)  # сложение

print(4 - 3)  #вычитание

print(3 * 4)  #умножение

print(4 ** 3)  # степень

print(4 / 3)  # деление

print(4 // 3)  # целая часть от деления

print(4 % 3) # остаток от деления

s = 3 + 4 # Обьект/ имя s ссылается на значение 3 + 4

memory_id = id(s)
print(s, memory_id)

s = 5 # Новая ссылка
print(s)

type # команда определения типа данных

type(3)

print(type(3))

print(type(3.4))
print(type('Молодец'))

a = 'Molodec'

print(type(a))

a = ['Molodec', 1, 'Круто', 6, 8]
print(type(a))

print(type(True))

print(type(False))

print(type(None))

a = input()
print(a)

a = input('Введите значение a:  ')
print(a)
print(type(a))

a = int(input('Введите значение a:  '))
print(a)
print(type(a))

a = 'Good' # Создание строки
b= 'Bad'

print(a + b)

print (a * 3)

c = 50
d = 10
print(f'Вставим числа (с) и (d)')

print(len(a))

a = [1, 3, 6]
print(a[0])

b = [8, 10, 11]

c = a + b
print (c)

print(c * 2)

c.append('Good')
print(c)

a.append(b)
print(a)

print(len(a))
