print("4-тапсырма. Сызықтық іздеу")
numbers = [int(x) for x in input("Массив элементтерін енгізіңіз (бос орын арқылы бөлінген): ").strip().split()]
text = input("Іздейтін сан: ").strip()
digits = text[1:] if text.startswith("-") else text
while not digits.isdigit():
    print("Қате: бүтін сан енгізіңіз.")
    text = input("Іздейтін сан: ").strip()
    digits = text[1:] if text.startswith("-") else text
target = int(text)

found_index = -1                              # -1: әзірге табылмады
for i in range(len(numbers)):
    if numbers[i] == target:
        found_index = i
        break                                 # табылды, іздеуді тоқтату

if found_index != -1:
    print(f"{target} саны массивте бар, индексі: {found_index}")
else:
    print(f"{target} саны массивте жоқ.")
print()