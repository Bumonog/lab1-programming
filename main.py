text = input("ВВедите строку: ")

print(f"Длинна: {len(text)}")
print(f"верхний регистр: {text.upper()}")
print(f"Нижний регистр: {text.lower()}")
print(f"Превый символ: {text[0]}")
print(f"Последний символ: {text[-1]}")
print(f"Кол-во пробелов: {text.count(' ')}")