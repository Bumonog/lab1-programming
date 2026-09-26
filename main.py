# Запрос данных с "Защитой от дурака"
while True:
    try:
        num_integer = int(input("Введите целое число:"))
        break
    
    except ValueError:
        print("Ошибка! Введите целое число!")
        
while True:
    try:
        num_float = float(input("Введите дробное число:"))
        break
    except ValueError:
        print("Ошибка! Введите дробное число!")

text = input("Введите строку:")

# Вывод типов данных переменных и их значений
print(f"Значение: {num_integer}, тип:{type(num_integer).__name__}")
print(f"Значение:{num_float}, тип:{type(num_float).__name__}")
print(f"Значение:{text}, тип:{type(text).__name__}")