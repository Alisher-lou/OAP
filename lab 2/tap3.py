print("3-тапсырма. Уақытты түрлендіру")
total_seconds = int(input("Тәулік басынан өткен секунд саны: "))

hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60

print(f"{total_seconds} секунд = {hours} сағат {minutes} минут {seconds} секунд")
print()