n = int(input("Введите число: "))
original = n
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num*10 + digit
    n //= 10
    
if original == reversed_num:
    print(f"{original} - палиндром")
else:
    print(f"{original} - не палиндром")