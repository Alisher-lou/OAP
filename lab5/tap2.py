print("2-тапсырма. Массивті өңдеу")
numbers = [int(x) for x in input("Массив элементтерін енгізіңіз (бос орын арқылы бөлінген): ").strip().split()]
total = 0
maximum = numbers[0]                          # бастапқы мән: бірінші элемент
minimum = numbers[0]
for x in numbers:
    total += x
    if x > maximum:
        maximum = x
    if x < minimum:
        minimum = x
average = total / len(numbers)

print("Элементтердің қосындысы:", total)
print("Ең үлкен элемент:", maximum)
print("Ең кіші элемент:", minimum)
print(f"Арифметикалық орта: {average:.2f}")
print()