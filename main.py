import random

N = int(input("Введите N: "))
numbers = [random.randint(1, 100) for _ in range(N)]

print(f"Исходный список чисел: {numbers}")
print(f"Сумма: {sum(numbers)}")
print(f"Среднее значение: {sum(numbers) / N}")
print(f"Минимальное значение: {min(numbers)}")
print(f"Максимальное значение: {max(numbers)}")

#сортировка списка
numbers.sort()
print(f"Отсортированный список чисел: {numbers}")

#удаление дубликатов (с сохранением порядка)
unique = list(dict.fromkeys(numbers))
print(f"Список без дубликатов: {unique}")