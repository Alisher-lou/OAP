def analyze_text(text):
    """Мәтіннің ұзындығын, сөз санын және бос орын емес таңбалар санын қайтарады."""
    length = len(text)
    words = text.split()
    letters = 0
    for ch in text:
        if not ch.isspace():
            letters += 1
    return length, len(words), letters


def search_word(text, query):
    """Сөзді регистрге тәуелсіз іздейді: алғашқы индекс пен кездесу саны."""
    if query.strip() == "":
        return -1, 0
    low_text = text.lower()
    low_query = query.lower()
    position = low_text.find(low_query)
    amount = low_text.count(low_query)
    return position, amount


def replace_word(text, old, new):
    """old сөзін new сөзіне алмастырған жаңа жолды қайтарады."""
    return text.replace(old, new)


def check_code(code):
    """Кодтың XX-999 үлгісіне сәйкестігін тексереді (X - латын бас әрпі, 9 - цифр)."""
    code = code.strip()
    if len(code) != 6:
        return False
    for ch in code[:2]:
        if not ("A" <= ch <= "Z"):
            return False
    if code[2] != "-":
        return False
    if not code[3:].isdigit():
        return False
    return True


def report(text, query, old, new, code):
    length, words, letters = analyze_text(text)
    print("Мәтін:", repr(text))
    print("Ұзындығы:", length)
    print("Сөз саны:", words)
    print("Бос орын емес таңбалар:", letters)
    position, amount = search_word(text, query)
    if position == -1:
        print("Іздеу сөзі '" + query + "' табылмады: индекс -1, саны", amount)
    else:
        print("Іздеу сөзі '" + query + "': алғашқы индекс", position, "| саны", amount)
    if old in text:
        print("Алмастырудан кейін:", replace_word(text, old, new))
    else:
        print("Алмастыру: '" + old + "' сөзі мәтінде жоқ, мәтін өзгерген жоқ")
    if check_code(code):
        print("Код", code, "- дұрыс пішім")
    else:
        print("Код", code, "- қате пішім")
    print("-" * 40)

TEXT = "Студенттер Python тілін зертханада үйренеді. Python пайдалы."
QUERY = "Python"
OLD = "пайдалы"
NEW = "қызықты"
CODE = "AB-123"

print("=== Тест 1. Негізгі тапсырма (қалыпты мәтін) ===")
report(TEXT, QUERY, OLD, NEW, CODE)
print("=== Тест 2. Бос жол ===")
report("", QUERY, OLD, NEW, CODE)
print("=== Тест 3. Тек бос орындар ===")
report("   ", QUERY, OLD, NEW, CODE)
print("=== Тест 4. Іздеу сөзі табылмайды ===")
report(TEXT, "Java", OLD, NEW, CODE)
print("=== Тест 5. Қате код ===")
report(TEXT, QUERY, OLD, NEW, "A1-12B")
