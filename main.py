numbers = input("Введите числа через запятую (например: 2, 5, 67, 52): ")
numbers = numbers.split(', ')
numbers = sorted([int(num) for num in numbers])

# находим медиану

## если четное количество элементов
if len(numbers)%2 ==0:
    median1 = numbers[len(numbers)//2 - 1]
    median2 = numbers[len(numbers)//2]
    print(f"Медиана равна {(median1 + median2)/2:.2f}")
    
## если нечётное количество элементов
else:
    print(f"Медиана равна {numbers[len(numbers)//2]}")