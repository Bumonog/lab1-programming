age = int(input("Введите возраст: "))

if age < 0: print("Некорректный возраст.")
elif age <= 12: print("Ребёнок.")
elif age <= 17: print("Подросток.")
elif age <= 64: print("Взорслый")
else: print("Пожилой.")