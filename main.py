mail = input("Введтите адрес электронной почты: ")
mail1 = mail
mail1 = mail1.replace("@", "@ ").split()

if mail.count("@") == 1 and mail1[1].count(".") == 1:
    print(f"{mail} - валидный адрес электронной почты")
else:
    print(f"{mail} - невалидный адрес электронной почты")