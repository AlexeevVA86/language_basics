int_positive = int(input())
max_dig = 0

while int_positive > 0:
    digit = int_positive % 10
    if digit > max_dig:
        max_dig = digit
        if max_dig == 9:
            break
    int_positive = int_positive // 10

print(max_dig)