print("1-тапсырма. Массивті енгізу")
text = input("Элементтер саны n (n > 0): ").strip()
while not (text.isdigit() and int(text) > 0):
    print("Қате: n оң бүтін сан болуы тиіс.")
    text = input("Элементтер саны n (n > 0): ").strip()
n = int(text)

numbers = []                                  # бос массив (тізім)
for i in range(n):
    value = input(f"{i}-элемент: ").strip()
    digits = value[1:] if value.startswith("-") else value
    while not digits.isdigit():               # бүтін сан енгізілгенше қайталау
        print("Қате: бүтін сан енгізіңіз.")
        value = input(f"{i}-элемент: ").strip()
        digits = value[1:] if value.startswith("-") else value
    numbers.append(int(value))

print("Енгізілген массив:", numbers)
print()