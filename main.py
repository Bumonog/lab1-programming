seconds = int(input("введите кличество секунд: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print(f"Часы: {hours:02d} минуты: {minutes:02d} секунды: {seconds:02d}")