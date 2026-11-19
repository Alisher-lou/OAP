# 1-тапсырма. Сызықтық іздеу
# Кемінде 10 сан енгізіледі, мақсатты сан сызықтық іздеумен ізделеді


def linear_search(items, target):
    """(индекс, салыстыру саны) қайтарады. Мән табылмаса, индекс -1."""
    comparisons = 0
    for i in range(len(items)):
        comparisons += 1
        if items[i] == target:
            return i, comparisons
    return -1, comparisons


def read_numbers(min_count=10):
    """Бір жолдағы бүтін сандарды оқиды; қате болса, қайта сұрайды."""
    while True:
        text = input(f"Кемінде {min_count} бүтін санды бос орынмен енгізіңіз: ")
        try:
            numbers = [int(x) for x in text.split()]
        except ValueError:
            print("Қате: тек бүтін сандарды енгізіңіз.")
            continue
        if len(numbers) < min_count:
            print(f"Қате: кемінде {min_count} сан керек, енгізілгені {len(numbers)}.")
            continue
        return numbers


def read_target():
    while True:
        try:
            return int(input("Ізделетін сан: "))
        except ValueError:
            print("Қате: бүтін сан енгізіңіз.")


def show_result(name, result):
    index, comparisons = result
    if index == -1:
        print(f"{name}: мән табылмады, салыстыру саны = {comparisons}")
    else:
        print(f"{name}: индекс = {index}, салыстыру саны = {comparisons}")


if __name__ == "__main__":
    numbers = read_numbers(10)
    target = read_target()
    print("Тізім:", numbers)
    show_result("Сызықтық іздеу", linear_search(numbers, target))