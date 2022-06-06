a = float(input("сколько заработал тенге "))
b = float(input("сколько потратил тенге "))
res = a - b
if res > 0:
    print(f"в общаг вложи {res} тенге")
    print(f"да ты комерс на все  {100 * (res / b): .1f}%")
    bratki = int(input("А сколько у тебя братков? "))
    print(f"если поделить общак то каждомы по {res / bratki:.3f} тенге.")
elif res < 0:
    print(f"да ты в минус {-res} тенге сработал!")
else:
    print("Общаг нулём не пополненишь")