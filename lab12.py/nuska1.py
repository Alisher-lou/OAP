import json
import os

KEY_NAME = "аты"
KEY_VALUE = "баға"


def read_lines(path):
    """Файлды оқиды. Файл жоқ болса, хабарлама шығарып None қайтарады."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print("Қате: '" + path + "' файлы табылмады.")
        return None


def count_lines_and_words(lines):
    """А тапсырмасы: бос емес жолдар саны және барлық сөздер саны."""
    non_empty = 0
    words = 0
    for line in lines:
        text = line.strip()
        if text == "":
            continue
        non_empty += 1
        words += len(text.replace(",", " ").split())
    return non_empty, words


def parse_records(lines):
    """Жолдарды жазбаларға (dict) айналдырады. Қате жолды өткізіп, хабарлама шығарады."""
    records = []
    for number, line in enumerate(lines, start=1):
        text = line.strip()
        if text == "":
            continue
        parts = text.split(",")
        if len(parts) != 2:
            print("Ескерту: " + str(number) + "-жол қате пішімде, өткізілді:", text)
            continue
        name = parts[0].strip()
        try:
            value = int(parts[1].strip())
        except ValueError:
            print("Ескерту: " + str(number) + "-жолда сан қате, өткізілді:", text)
            continue
        records.append({KEY_NAME: name, KEY_VALUE: value})
    return records


def calculate(records):
    """Ә тапсырмасы: Орташа баға және 50-ден жоғары алғандар саны."""
    if not records:
        return ["Деректер жоқ: есептеу мүмкін емес (нөлге бөлу болмайды)."]
    values = [r["баға"] for r in records]
    average = sum(values) / len(values)
    above = [r["аты"] for r in records if r["баға"] > 50]
    return [f"Жазбалар саны: {len(records)}",
            f"Орташа баға: {average:.1f}",
            f"50-ден жоғары алғандар саны: {len(above)} ({', '.join(above)})"]


def write_report(path, non_empty, words, results):
    with open(path, "w", encoding="utf-8") as file:
        file.write("ЕСЕП: Студент бағалары\n")
        file.write(f"Бос емес жолдар саны: {non_empty}\n")
        file.write(f"Барлық сөздер саны: {words}\n")
        for row in results:
            file.write(row + "\n")


def save_json(path, records):
    """Б тапсырмасы: жазбаларды JSON массиві ретінде сақтау."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def process(input_path, report_path, json_path):
    lines = read_lines(input_path)
    if lines is None:
        return None
    non_empty, words = count_lines_and_words(lines)
    print("Бос емес жолдар:", non_empty, "| Сөздер:", words)
    records = parse_records(lines)
    results = calculate(records)
    for row in results:
        print(row)
    write_report(report_path, non_empty, words, results)
    save_json(json_path, records)
    restored = load_json(json_path)
    print("JSON-нан жүктелген жазбалар саны:", len(restored))
    if restored:
        print("Бірінші жазбаның '" + KEY_NAME + "' өрісі:", restored[0][KEY_NAME])
    print("Жүктелген деректер бастапқымен сәйкес пе:", restored == records)
    return records


print("===== Тест 1. Негізгі файл (5 дұрыс жазба) =====")
process("input.txt", "report.txt", "data.json")

# Тест файлдары tests қалтасында жасалады
os.makedirs("tests", exist_ok=True)

print()
print("===== Тест 2. Бос файл =====")
with open("tests/empty.txt", "w", encoding="utf-8") as f:
    f.write("")
process("tests/empty.txt", "tests/report_empty.txt", "tests/data_empty.json")

print()
print("===== Тест 3. Файл жоқ =====")
process("tests/no_such_file.txt", "tests/report_none.txt", "tests/data_none.json")

print()
print("===== Тест 4. Бір қате жазба =====")
with open("tests/bad.txt", "w", encoding="utf-8") as f:
    f.write("Айдана,85\nЕржан,abc\nМадина,94\n")
process("tests/bad.txt", "tests/report_bad.txt", "tests/data_bad.json")

print()
print("===== Тест 5. Қазақша мәтін (UTF-8) =====")
with open("data.json", "r", encoding="utf-8") as f:
    json_lines = f.read().splitlines()
print("data.json файлының алғашқы жолдары:")
for row in json_lines[:5]:
    print(row)
