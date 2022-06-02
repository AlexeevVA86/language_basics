revenue = float(input("сколько заработал тенге "))
costs = float(input("сколько потратил тенге "))
result = revenue - costs
if result > 0:
    print(f"в общаг вложи {result} тенге")
    print(f"да ты комерс на все  {100 * (result / costs): .1f}%")
    personal_n = int(input("А сколько у тебя братков? "))
    print(f"если поделить общак то каждомы по {result / personal_n:.3f} тенге.")
elif result < 0:
    print(f"да ты в минус {-result} тенге сработал!")
else:
    print("Общаг нулём не пополненишь")