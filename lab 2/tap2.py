print("2-тапсырма. Арифметикалық өрнек")
x = float(input("Бірінші сан: "))
y = float(input("Екінші сан: "))
z = float(input("Үшінші сан: "))

total = x + y + z
average = total / 3
product = x * y * z
square = x ** 2

print(f"Қосынды: {total:.2f}")
print(f"Арифметикалық орта: {average:.2f}")
print(f"Көбейтінді: {product:.2f}")
print(f"Бірінші санның квадраты: {square:.2f}")
print()