my_list = [9, 7, 5, 3, 1]
while my_list != 0:
    count = 0
    a = int(input("Введите число: "))
    for i in my_list:

        if a <= i:
            count += 1
    my_list.insert(count, a)
    print(my_list)
