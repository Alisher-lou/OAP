print("3-тапсырма. Шарт бойынша санау")
numbers = [int(x) for x in input("Массив элементтерін енгізіңіз (бос орын арқылы бөлінген): ").strip().split()]
positive = 0
negative = 0
even = 0
for x in numbers:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    if x % 2 == 0:                            # 0 да жұп сан болып саналады
        even += 1

print("Оң сандар саны:", positive)
print("Теріс сандар саны:", negative)
print("Жұп элементтер саны:", even)
print()