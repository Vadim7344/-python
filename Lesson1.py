# Задание №1
a = input("Назовите свое имя: ")
b = input("А теперь, хорошо бы узнать фамилию: ")
print("Хорошего вам дня", a, b)
# Задание №2
time = int(input('Введите ваше время в секундах, а я его переведу в часы и минуты: '))
hour = time // 3600
minute = (time % 3600) // 60
second = time % 60
print(hour, ':', minute, ':', second)
# Задание №3
a = input('Введите число от 0 до 9: ')
print(int(a) + int(a+a) + int(a+a+a))
# Задание 4
num = int(input('Введите натуральное число: '))
num_last = 0 # цифра в числе, начиная с последней
n = 1 #степень 10-ки для прохода по всем цифрам числа
while num > (10 ** n):
    num_last = (num % (10 ** n)) // (10 ** (n-1)) # это выражение должно проверять все цифры нашего числа
    n = n + 1
if num_last == 9:
    print('Наибольшая цифра введенного числа 9')
else:
    print('Наибольшая цифра введенного числа ', num_last)
#вроде бы что касается цикла while, я понял как проверить все цифры в числе, но не дошел, как выбрать из них максимальную
#Задание 5
income = float(input('Выручка фирмы составляет: '))
costs = float(input('Выручка фирмы составляет: '))
a = income - costs
if a >= 0:
    print('Прибыль компании составляет: ', a)
    print('Рентабельность компании составляет: ', a / income)
    workers = int(input('Введите число сотрудников:  '))
    print('Прибыль на одного сотрудника составляет', a / workers)
else:
    print('Компания работает с убытком: ', a)
#Задание №6
first_run = int(input('Сколько спортсмен пробежал в 1-й день: '))
last_run = int(input('Сколько спортсмен пробежал в последний день: '))
day =1
while first_run < last_run
    first_run = 1.1 * first_run
    day = day + 1
print('Спортсмен достигнет результата на день номер ', day)



