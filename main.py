a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию(+, -, *, /): ").strip()

match operation:
    case "+":
        print(f"Результат: {a + b}")
    case "-":
        print(f"Результат: {a - b}")
    case "*":
        print(f"Резуьтат: {a * b}")
    case "/":
        if b==0: print("ОшибкаЖ на ноль делить нельзя.")
        else: print(f"Результат: {a/b:.2f}")
