# 1-тапсырма: үш бүтін санның ең үлкенін анықтау
# Құрама және кірістірілген шарттар, тең мәндерді тексеру

a_s = input("Бірінші сан: ").strip()
b_s = input("Екінші сан: ").strip()
c_s = input("Үшінші сан: ").strip()

# Кіріс деректерін тексеру: бүтін сан болуы керек (минус таңбасы рұқсат)
a_t = a_s[1:] if a_s.startswith("-") else a_s
b_t = b_s[1:] if b_s.startswith("-") else b_s
c_t = c_s[1:] if c_s.startswith("-") else c_s

if not (a_t.isdigit() and b_t.isdigit() and c_t.isdigit()):
    print("Қате енгізу: бүтін сан енгізу керек")
else:
    a = int(a_s)
    b = int(b_s)
    c = int(c_s)
    if a == b and b == c:                 # құрама шарт
        print("Үш сан тең:", a)
    elif a >= b and a >= c:
        if a == b or a == c:              # кірістірілген шарт
            print("Ең үлкен сан:", a, "(тең мәндер бар)")
        else:
            print("Ең үлкен сан:", a)
    elif b >= a and b >= c:
        if b == c:                        # кірістірілген шарт
            print("Ең үлкен сан:", b, "(тең мәндер бар)")
        else:
            print("Ең үлкен сан:", b)
    else:
        print("Ең үлкен сан:", c)