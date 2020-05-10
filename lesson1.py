# some_vars = "HELLO WORLD"  # str строка
#
# """
# Привет
# Это несколько
# строк
# комментария
# """
#
# some_vars_2 = 'Hello world'
# home_number = 22  # int целое число
# var_float = 22.646  # float дробное число
# var_bool = True
# var_bool_2 = False
#
# var_none = None
#
# print(some_vars)


name = input('Ваше имя?\n')
print('Добрый вечер', name)

while True:
    age = input('Сколько вам лет?')
    if age.isdigit():
        age = int(age)
        break
    else:
        print('Ошибка ввода, введите только число')




#
# i = 0
# while i < 10:
#     print(i)
#     if i == 4:
#         break
#     # if i == 3:
#     #     i += 2
#     #     continue
#     # i = i + 1
#     print('#' * 10)
#     i += 1
# else:
#     print('WHILE ELSE')
