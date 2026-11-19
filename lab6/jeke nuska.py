def is_valid_sides(length, width):
    """Қабырғалар оң сан болса True қайтарады."""
    return length > 0 and width > 0


def perimeter(length, width):
    if not is_valid_sides(length, width):
        return None
    return 2 * (length + width)


def area(length, width):
    if not is_valid_sides(length, width):
        return None
    return length * width


def diagonal(length, width):
    if not is_valid_sides(length, width):
        return None
    return (length ** 2 + width ** 2) ** 0.5


def read_positive(prompt):
    """Оң сан енгізілгенше сұрауды қайталайды (енгізу функциясы)."""
    while True:
        text = input(prompt).strip()
        if text.replace(".", "", 1).isdigit() and float(text) > 0:
            return float(text)
        print("Қате: оң сан енгізіңіз.")


# ========== Тестілеу (assert) ==========
def run_tests():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-4) == 16

    assert round(average(4, 7, 10), 2) == 7.00
    assert round(average(1, 2, 2), 2) == 1.67
    assert round(average(-3, 0, 3), 2) == 0.00

    assert is_passed(49) is False
    assert is_passed(50) is True
    assert is_passed(100) is True
    assert is_passed(101) is None
    assert is_passed(-5) is None

    assert power(6) == 36
    assert power(2, 5) == 32
    assert power(-3, 3) == -27

    assert subtotal(2500, 3) == 7500
    assert discount_amount(7500, 0.10) == 750
    assert final_price(2500, 3, 0.10) == 6750
    assert final_price(2500, 3, 0) == 7500        # 0% жеңілдік
    assert final_price(2500, 3, 1) == 0           # 100% жеңілдік
    assert final_price(2500, 1, 0.10) == 2250     # quantity = 1

    assert perimeter(3, 4) == 14
    assert area(3, 4) == 12
    assert diagonal(3, 4) == 5
    assert perimeter(2.5, 4) == 13
    assert area(2.5, 4) == 10
    assert round(diagonal(2.5, 4), 2) == 4.72
    assert perimeter(1, 1) == 4
    assert round(diagonal(1, 1), 2) == 1.41
    assert area(0, 5) is None                     # қате дерек
    assert diagonal(-3, 4) is None                # қате дерек
    print("Барлық assert тестілері сәтті өтті.")


# ========== Негізгі бағдарлама ==========
def main():
    print("1-тапсырма:", square(5), square(0), square(-4))

    print("2-тапсырма:")
    for a, b, c in [(4, 7, 10), (1, 2, 2), (-3, 0, 3)]:
        print(f"  average({a}, {b}, {c}) = {average(a, b, c):.2f}")

    print("3-тапсырма:")
    for score in [49, 50, 100, 101]:
        result = is_passed(score)
        if result is None:
            print(f"  {score}: қате, балл 0 мен 100 аралығында болуы тиіс")
        else:
            print(f"  {score}: {result}")

    print("4-тапсырма:", power(6), power(2, 5), power(-3, 3))

    print("5-тапсырма:")
    print("  2500 x 3, 10%:", final_price(2500, 3, 0.10))
    print("  2500 x 3, 0%:", final_price(2500, 3, 0))
    print("  2500 x 3, 100%:", final_price(2500, 3, 1))
    print("  2500 x 1, 10%:", final_price(2500, 1, 0.10))

    print()
    run_tests()

    print()
    print("Жеке нұсқа 1. Тік төртбұрыш")
    length = read_positive("Ұзындығы: ")
    width = read_positive("Ені: ")
    print(f"Периметр: {perimeter(length, width):.2f}")
    print(f"Аудан: {area(length, width):.2f}")
    print(f"Диагональ: {diagonal(length, width):.2f}")