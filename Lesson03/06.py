# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
# и возвращающую их же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(*args):
    return str(args).title()


print(int_func('qqqqq', 'aaaaa', 'ffffff', 'ttttt'))
