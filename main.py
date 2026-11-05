matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# транспонирование матрицы с помощью zip
transponed = [ list(row) for row in zip(*matrix) ]

# вывод
print("Исходная матрица:")
for row in matrix:
    print(row)
    
print("\nТранспонированная матрица:")
for row in transponed:
    print(row)