year = int(input('Введите год: '))

if year % 4 != 0:
    print(False)

elif year % 100 == 0:
    if year % 400 == 0:
        print(True)
    else:
        print(False)
else:
    print(True)