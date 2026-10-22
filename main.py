n = int(input("Введите целое число N: "))

a, b = 0, 1

print(f"Первые {n} чисел ФИбоначчи: ")
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b