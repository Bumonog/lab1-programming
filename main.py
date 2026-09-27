print("""Конвертер температур
      1. Из °C в °F
      2. Из °F в °C""")

choice = int(input("Ваш выбор(введите 1/2): "))

if choice == 1:
    celsius = float(input("Введите температуру в °C: "))
    fathrenheit = celsius * 9/5 + 32
    print(f"{celsius:.1f}°C = {fathrenheit:.1f}°F")
elif choice == 2:
    fathrenheit = float(input("Введите температуру в °F: "))
    celsius = (fathrenheit - 32) * 5/9
    print(f"{fathrenheit:.1f}°F = {celsius:.1f}°C")
else:
    print("Некорректный ввод.")