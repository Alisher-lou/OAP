def unique_info(items):
    """А тапсырмасы: бірегей мәндер жиыны және қайталанатын элементтер саны."""
    unique = set(items)
    duplicates = len(items) - len(unique)
    return unique, duplicates


def frequency(items):
    """Ә тапсырмасы: әр мәннің кездесу жиілігі (dict)."""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq


def most_common(freq):
    """Ең жиі кездесетін мән(дер). Теңдік болса, бәрі қайтарылады."""
    if not freq:
        return [], 0
    top = max(freq.values())
    leaders = []
    for key, value in freq.items():
        if value == top:
            leaders.append(key)
    return leaders, top


def find_record(records, field, value):
    """Б тапсырмасы: өріс мәні бойынша жазбаны іздеу."""
    for record in records:
        if record.get(field) == value:
            return record
    return None


def update_record(records, key_field, key_value, field, new_value):
    """Бір жазбаның бір өрісін жаңарту."""
    record = find_record(records, key_field, key_value)
    if record is None:
        return False
    record[field] = new_value
    return True


def filter_records(records, field, sign, limit):
    """Шартқа сәйкес жазбаларды іріктеу."""
    result = []
    for record in records:
        value = record.get(field)
        if value is None:
            continue
        if sign == ">" and value > limit:
            result.append(record)
        elif sign == "<" and value < limit:
            result.append(record)
    return result


def show_analysis(title, items):
    """В тапсырмасы: нәтижені түсінікті түрде шығару."""
    print("---", title, "---")
    print("Тізім:", items)
    unique, duplicates = unique_info(items)
    print("Жалпы элементтер саны:", len(items))
    print("Бірегей мәндер (сұрыпталған):", sorted(unique))
    print("Бірегей мәндер саны:", len(unique))
    print("Қайталанатын элементтер саны:", duplicates)
    freq = frequency(items)
    print("Жиілік сөздігі:", freq)
    leaders, top = most_common(freq)
    if leaders:
        print("Ең жиі кездесетін:", ", ".join(leaders), "-", top, "рет")
    else:
        print("Ең жиі кездесетін: жоқ (тізім бос)")


def print_records(records):
    if not records:
        print("  (жазба жоқ)")
    for record in records:
        print(" ", record)
items = ['роман', 'детектив', 'фантастика', 'роман', 'поэзия', 'детектив', 'роман', 'тарих', 'фантастика', 'роман', 'поэзия']  # кітап жанрлары

records = [
    {'атауы': 'Дала әуені', 'жанры': 'роман', 'жылы': 2018},
    {'атауы': 'Құпия хат', 'жанры': 'детектив', 'жылы': 2021},
    {'атауы': 'Жұлдызға сапар', 'жанры': 'фантастика', 'жылы': 2023},
    {'атауы': 'Көктем жыры', 'жанры': 'поэзия', 'жылы': 2015},
    {'атауы': 'Ұлы Жібек жолы', 'жанры': 'тарих', 'жылы': 2022}
]

print("========== А және Ә тапсырмалары ==========")
show_analysis("Кітап жанрлары", items)
print()
print("========== Б тапсырмасы ==========")
print("Барлық жазбалар:")
print_records(records)

found = find_record(records, "атауы", 'Көктем жыры')
print("Іздеу (атауы = Көктем жыры):", found)
not_found = find_record(records, "атауы", "Белгісіз")
print("Іздеу (атауы = Белгісіз):", "табылмады" if not_found is None else not_found)

old_value = found["жылы"]
update_record(records, "атауы", 'Көктем жыры', "жылы", 2024)
print("Жаңарту: «Көктем жыры» жазбасының «жылы» өрісі", old_value, "->", found["жылы"])
print("Жаңартудан кейінгі жазба:", found)

selected = filter_records(records, "жылы", ">", 2020)
print("Іріктеу: 2020 жылдан кейінгі кітаптар (жылы > 2020):")
print_records(selected)
print("Іріктелген жазбалар саны:", len(selected))

print()
print("========== В тапсырмасы: тестілеу ==========")
show_analysis("Тест 1. Қайталанатын мәндер", items)
show_analysis("Тест 2. Барлық мән әртүрлі", ['детектив', 'поэзия', 'роман', 'тарих', 'фантастика'])
show_analysis("Тест 3. Барлық мән бірдей", ['роман', 'роман', 'роман', 'роман'])
show_analysis("Тест 4. Бос тізім", [])
print("--- Тест 5. Жоқ кілтпен іздеу ---")
print("records[0].get(\"автор\", \"көрсетілмеген\") ->", records[0].get("автор", "көрсетілмеген"))
print("Бос тізімде сүзу:", filter_records([], "жылы", ">", 2020))



