valid = False
while valid == False:
    try:
        N = int(input("Введите высоту треугольника Паскаля: "))
        if N <= 0:
            raise ValueError
        valid = True
    except ValueError:
        print("-"*50)
        print(f"| {"Ошибка: введите натуральное число.":^48}|")
        print("-"*50)

# строим треугольник
row = [1]
rows = []

for _ in range(N):
    rows.append(row)
    new_row = [1]                               # Цифра 1 всегда первая
    for i in range(len(row) - 1):
        new_row.append(row[i] + row[i + 1])     # Элемент равен сумме двух элементов над ним
    new_row.append(1)                           # Цифра 1 всегда последняя

    row = new_row
# находим ширину последней строки
last_line = ""
for number in rows[-1]:
    last_line += str(number) + "   "
width = len(last_line)

# выводим строки по центру
for row in rows:
    line = ""
    for number in row:
        line += str(number) + "   "
    print(line.center(width))