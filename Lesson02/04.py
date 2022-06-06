my_str = input('Пользователь вводит строку из нескольких слов. ')
my_list = my_str.split(' ')
for i, k in enumerate(my_list, 1):
    print(k[:10])
