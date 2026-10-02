print("Это программа для проверки, является ли число палиндромом.")
Number = int(input('Введите число: '))
num = Number
count = 0

while num > 0:
    count += 1
    num //= 10

for i in range(count):
    first = Number // 10**(count-i-1)   # Получаем первую цифру
    last = Number % 10                  # Получаем последнюю цифру
    Number -= first * 10**(count-i-1)   # Удаляем первую цифру
    Number //= 10                       # Удаляем последнюю цифру
    count -= 1 
    if first != last: 
        print('Не палиндром')
        break
else:
    print('Палиндром')

print('END')