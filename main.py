a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a >= b and a >= c: maximum = a
elif b>=a and b>=c: maximum = b
else: maximum = c

print(f"Максимум: {maximum}")