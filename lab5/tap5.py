print("5-тапсырма. Шамасы бойынша екінші элемент")
numbers = [int(x) for x in input("Массив элементтерін енгізіңіз (бос орын арқылы бөлінген): ").strip().split()]
if len(numbers) < 2:
    print("Массивте 2-ден аз элемент бар, екінші элементті анықтау мүмкін емес.")
else:
    first = numbers[0]                        # ең үлкен мән
    second = None                             # екінші мән (әзірге жоқ)
    for x in numbers:
        if x > first:
            second = first
            first = x
        elif x < first and (second is None or x > second):
            second = x
    if second is None:
        print("Барлық элементтер тең, екінші элемент жоқ.")
    else:
        print("Шамасы бойынша екінші элемент:", second)