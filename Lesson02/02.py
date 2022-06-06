string_task = input('введите значения через пробел ')
list_task = string_task.split(' ')
i = 0
while i < len(list_task[:-1]):
    list_task[i], list_task[i + 1] = list_task[i + 1], list_task[i]
    i += 2
print('Cписок выглядит так: ', list_task)
