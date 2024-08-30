first = int(input("Введите первое значение: "))
second = int(input("Введите второе значение: "))
third = int(input("Введите третье значение: "))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)