# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
#  и возвращает сумму наибольших двух аргументов.

def my_func(num_a, num_b, num_c):
    return sum(sorted([num_a, num_b, num_c])[1:])


print(my_func(33, 11, 44))
