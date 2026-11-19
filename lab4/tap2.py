# 2-тапсырма. Шарты соңынан тексерілетін цикл (while True және break арқылы)
# Цикл денесі кемінде бір рет орындалады, 100-ден үлкен сан енгізілгенде ғана тоқтайды

while True:
    text = input("100-ден үлкен сан енгізіңіз: ").strip()
    digits = text[1:] if text.startswith("-") else text

    if not digits.replace(".", "", 1).isdigit():
        print("Қате: сан енгізу керек.")
        continue                      # келесі итерацияға өту

    number = float(text)
    if number > 100:                  # шығу шарты СОҢЫНДА тексеріледі
        break
    print(number, "саны 100-ден үлкен емес. Қайта енгізіңіз.")

print("Қабылданған сан:", number)