

def problem(num):
    print(F"Problem {num}")

#                                   First File
# Problem 1
problem(1)

# 1.Что больше: Количество троек в числе 17531 или число 5821?
first_ = '17531'
second = 5821
count_3 = 0
for i in first_:
    if i == '3':
        count_3 = count_3 + 1
if count_3 > second:
    print(count_3, ' больше')
elif second > count_3:
    print(second, ' больше')
else:
    print(count_3, ' равно ', second)
# 2.Если остаток деления 4388 на 7 больше или равно 4 - умножьте остаток на 7.
if 4388 % 7 >= 4:
    print((4388 % 7) * 7)
#3.Если остаток деления 4292 на 5 меньше или равно 3 - разделите остаток на 3.
if 4292 % 5 <= 3:
    print((4292 % 5) / 3)
#4.Распишите по порядку шаги исполнения выражения: 7 + 5 * (3 * (27**3))
# 1. (27**3))
# 2. * 3
# 3. * 5
# 5. + 7

# 5.Сколько получится если:
#   1. От 183 отнять 17
#   2. Разделить 19
#   3. Добавить 13.6
#   4. Результат умножить на 2
#   5. И всё это поделить по модулю 12
print(((((183 - 17) / 19) + 13.6) * 2) % 12 )



# Problem 2
problem(2)

calculator = input('choose operation : + ,-, / ,* ,, //, %')

a = float(input('first number'))

b = float(input('second operation'))

if calculator == '+':
        c = a + b
        print('resulst' + str(c))
elif calculator == '/':
        c = a / b
        print('results' + str(c))
elif calculator == '//':
        c = a // b
        print('results' + str(c))
elif calculator == '':
        print('results' + str(c))
elif calculator == '-':
        c = a - b
        print('results' + str(c))
elif calculator == '%':
        c = a % b
        print('results' + str(c))



# Problem 3
problem(3)
user_list = []

for i in range(0, 2):
    item = input()
    user_list.append(item)

print("You registered successfully!\n Please Log in: ")

while 1:
    login = input()
    password = input()
    if user_list[0] == login and user_list[1] == password:
        print("You are logged in.")
        break
    else:
        print("username or password is inccorect!")



# Problem 4
problem(4)

interview_list2 = []
interview_list1 = [
    "Please enter required age: ",
    "Plaese enter required experience YRS: ",
    "Please enter expected salary: "
]

print("Please enter required language: ")
language = input()

for i in range(0, 3):
    print(interview_list1[i])
    item = int(input())
    interview_list2.append(item)

if (language == "python" or language == "java" or language == "javascript") and (interview_list2[0] >= 18 or interview_list2[0] <= 65) and (interview_list2[1] >= 3) and interview_list2[2] <= 60000:
    print("You are right for this job!!")
else:
    print("You are not fine for this job learn more please.")



# Problem 5
problem(5)

summ = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        summ += i

print(summ)



# Problem 6
problem(6)
numbers = 4729461084
x = [int(a) for a in str(numbers)]
print(x)
print(sum(x))

# Problem 7
problem(7)

# Седьмое Задание
# Выбор компьютера
# Написать программу по выбору компьютера.
# Нужен компьютер от 4 до 8 GB оперативной памяти.
# Размер жесткого диска как минимум 256, если SSD. Если HDD, то как минимум 1 террабайт.
# Стоимость ноутбука не должна превышать 1000$.

dict = {'Вид компютера': 'Ноутбук ПК'}
print(type(dict))
dict.update({'Размер оперативнов памяти':input('Выберите размер оперативной памяти')})
dict.update({'Тип жесткого диска': input('Выберите тип жесткого диска')})
dict.update({dict['Тип жесткого диска']: input('Выберите размер жетского диска')})
dict.update({'Стоимость ноутбука': input('сколько стоит ноутбук')})
print(dict)

if dict['Тип жесткого диска'] == 'HDD':
    if int(dict['HDD']) <= 1024:
        print('Размер HDD меньше 1 терабайта')
    else:
        print('размер HDD больше 1 терабайта')

if dict['Тип жесткого диска'] == 'SSD':
    if int(dict['SSD']) <= 256:
        print('Размер SSD меньше 256 гигабайта')
    else:
        print('размер HDD больше 256 гигабайта')


if int(dict['Стоимость ноутбука']) <= 1000:
    print('Стоимость не превышает 1000$')
else:
    print('Стоимость превысила 1000$' )


# Problem 8
problem(8)

a = [1, 1, 2, 3,13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
a.append(13)
b = 28 * 100 / 40
print(a)
print(a.count(13))
print(len(a))
if b == 70.0:
        print('совпадение? не думаю')
if b < 70.0:
        print('неужели')
if b > 70.0:
        print('я так и знал')



#                                   Second File 

# Problem 1
problem(1)

f = 10

r = 10.5

j = 13.7

a = r > j

b = r < j

c = r == j

if  '>' :
        a = r > j 
        print('results:' + str(a) + ' r > j ' )

if '<':
        b = r < j
        print('results:' + str(b) + ' r < j ') 
else:
        c = r == j
        print('results:' + str(c) + 'r == j')



# Problem 2
problem(2)

a = 4
b = 7
if a % 2 == 0:
        print('четное число')
if a % 2 != 0:
        print('число простое')
print('Число А положительное или простое')



# Problem 3
problem(3)
a = 123
b = 321
d = (a+b)
if d/2:
        print(d/2)
if d/2<b:
        print('b > sum/2 > a')



# Problem 4
problem(4)
a = 35
b = 25
c = 75
max, min = 0, 0

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c


if a < b and a < c:
    min = a
elif b < a and b < c:
    min = b
else:
    min = c

print(max)
print(min)


