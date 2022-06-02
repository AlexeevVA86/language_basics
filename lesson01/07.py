while True:
    days = 1
    sta = float(input("start: "))
    las = float(input("finish: "))
    if sta <= 0 or las < 0:
        print("значение меньше нуля спортсмен диградирует")
    else:
        while sta < las:
            sta += sta * 0.1
            days += 1

        print(f"результат будет достигнут за {days} дней")
        break