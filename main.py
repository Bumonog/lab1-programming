mail = input("Введтите адрес электронной почты: ")
mail1 = mail
mail1 = mail1.replace("@", "@ ").split()

if len(mail) <= 254 and len(mail1[0][:-1]) <=64 and all( s not in mail for s in " ,()'/\"!$" ) and mail.count("@") == 1 and mail1[1].count(".") == 1:
    print(f"{mail} - валидный адрес электронной почты")
else:
    print(f"{mail} - невалидный адрес электронной почты")