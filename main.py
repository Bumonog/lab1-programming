list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# через множества
set1 = set(list1)
set2 = set(list2)

union = set1 | set2          # объединение
intersection = set1 & set2   # пересечение
difference = set1 - set2     # разность

# вывод
print(f"Объединение: {union}")
print(f"Пересечение: {intersection}")
print(f"разность: {difference}")