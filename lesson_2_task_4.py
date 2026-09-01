a = int (input ('Введите число:'))
if a <=1:
    a =3

for a in range(1,a):
    string = ' '
    if (a % 3 == 0):
        string = string + "Fizz"
    if (a % 5 == 0):
        string = string + "Buzz"
    if (a % 3 != 0 and a % 5 != 0):
        string = string + str(a)
    print(string, end = '')
    