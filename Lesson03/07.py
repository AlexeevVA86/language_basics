def str_is_lat(str0):
    '''Функция проверяющая, состоит ли строка из латинских букв и пробелов.'''
    result = True
    for el in str0:
        if el not in lat_str:
            result = False
            break
    return result


int_func = lambda str1: str1.title()

lat_str = 'qwertyuiopasdfghjklzxcvbnm '

while True:
    str2 = input('Введите одно или несколько слов латиницей с маленькой буквы: ')
    if str2.islower() and str_is_lat(str2):
        print(int_func(str2))
        break
    else:
        print('Ошибка! Используйте только латинские буквы в нижнем регистре.')
