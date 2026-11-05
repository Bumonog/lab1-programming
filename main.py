numbers = [1, 2, 3 ,2, 4, 5, 1, 6, 3, 7]

# поиск дубликатов
numbers1 = set(numbers)        # множество без повторяющихся чисел
for num in numbers1:
    count = numbers.count(num)
    if count > 1:
        print(f"Число {num} повторяется {count} раз(a).")
    