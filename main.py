N = int(input("Введите целое число: "))

sum_numbers = 0
product = 1
sum_squares = 0

for i in range(1,N+1):
    sum_numbers += i
    product *= i
    sum_squares += i**2
    
print(f"Сумма чисел: {sum_numbers}")
print(f"Произведение(N!): {product}")
print(f"Сумма квадратов чисел: {sum_squares}")