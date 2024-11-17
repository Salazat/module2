# Циклы

# функции

# практика

#for для перебора значений, цик со счетчиком
#while бесконечный перебор, не привязывается к последовательности, чикол без счетчика

# films =['Фильм 1', 'Фильм 2', 'Фильм 3', 'Фильм 4', 'Фильм 5']
# print(films)
# for film in films:
#     print(film)

# import random # random библиотека pyton
#
# num = random.randint(1,100) #randint случайные числа
#
# points = 100
# errorPoints = 0
#
# while points > errorPoints: #True = 1 > 0
#     answer = int(input('Введите число, которое я загадал: '))
#     if answer > num:
#         print('Мое число меньше')
#         errorPoints += 1
#     elif answer < num:
#         print('Мое число больше')
#         errorPoints += 1
#     else:
#         print('Вы угадали!')
#         break

# Функция это обособленный кусочек кода который

# def total_sun(num1, num2, num3 ): # Парметры в круглых скобках
#     result = num1 + num2 + num3
#     print(result)
#     if 5 > 0:
#         return '5 > 0'
#     else:
#         return result


# output_result = total_sun(1, 4, 5)# Аргументы
# print(output_result)

# num1 = 9
# print(num1)
#
#
# def test(): # Функция другая область
#     global num1 # Глобальная переменная!
#     print(num1)
#     num1 += 55
#     print(num1)
#
# test()
#
# print(num1)