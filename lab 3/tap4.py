# 4-тапсырма: қарапайым калькулятор (+, -, *, /)
# Нөлге бөлу және белгісіз амал шарттар арқылы өңделеді

x_s = input("Бірінші сан: ").strip()
op = input("Амал (+, -, *, /): ").strip()
y_s = input("Екінші сан: ").strip()

# Кіріс деректерін тексеру: сан болуы керек (минус және бөлшек рұқсат)
x_t = x_s[1:] if x_s.startswith("-") else x_s
y_t = y_s[1:] if y_s.startswith("-") else y_s

if not (x_t.replace(".", "", 1).isdigit() and y_t.replace(".", "", 1).isdigit()):
    print("Қате енгізу: сан енгізу керек")
elif op != "+" and op != "-" and op != "*" and op != "/":
    print("Қате: белгісіз амал")
else:
    x = float(x_s)
    y = float(y_s)
    if op == "+":
        print("Нәтиже:", x + y)
    elif op == "-":
        print("Нәтиже:", x - y)
    elif op == "*":
        print("Нәтиже:", x * y)
    else:
        if y == 0:                        # кірістірілген шарт
            print("Қате: нөлге бөлуге болмайды")
        else:
            print("Нәтиже:", x / y)