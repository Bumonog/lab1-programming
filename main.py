a, b  = float(input("Введите первое число: ")), float(input("Введите второе число: "))

print(f'Сумма: {a + b}')
print(f'Разность: {a - b}')
print(f'ПРоизведение: {a * b}')
print(f'Деление(2 знака после запятой): {a / b:.2f}')
print(f'Целочисленное деление: {a // b}')
print(f'Остаток: {a % b}')

try:
    print(f'Степнь: {a ** b:.2f}')
except OverflowError:
    print("Степень: cлишком большой результат.")