# 3-тапсырма. Екі алгоритмді бір бағдарламада салыстыру
# Мән бірінші, ортаңғы, соңғы орында және мүлде жоқ болған жағдайлар

from task1_linear import linear_search, read_numbers
from task2_binary import binary_search


def compare_table(original, sorted_copy, cases):
    print(f"{'Жағдай':<18}{'Мән':>6}   {'Сызықтық':<12}{'Екілік':<12}")
    for label, target in cases:
        lin = linear_search(original, target)
        bin_ = binary_search(sorted_copy, target)
        print(f"{label:<18}{target:>6}   {str(lin):<12}{str(bin_):<12}")


def run_tests():
    """Тапсырмадағы бақылау тестілері."""
    data = [2, 4, 6, 8, 10]
    assert linear_search(data, 2) == (0, 1)
    assert binary_search(data, 2) == (0, 2)
    assert linear_search(data, 8) == (3, 4)
    assert binary_search(data, 8) == (3, 2)
    assert linear_search(data, 11) == (-1, 5)
    assert binary_search(data, 11) == (-1, 3)
    assert linear_search([], 5) == (-1, 0)
    assert binary_search([], 5) == (-1, 0)
    assert linear_search([7], 7) == (0, 1)
    assert binary_search([7], 7) == (0, 1)
    print("Барлық бақылау тестілері сәтті өтті (10 тексеріс).")


if __name__ == "__main__":
    numbers = read_numbers(10)
    sorted_numbers = sorted(numbers)
    print("Бастапқы тізім:", numbers)
    print("Сұрыпталған көшірме:", sorted_numbers)
    compare_table(numbers, sorted_numbers, [
        ("Бірінші орында", numbers[0]),
        ("Ортаңғы орында", numbers[len(numbers) // 2]),
        ("Соңғы орында", numbers[-1]),
        ("Тізімде жоқ", sorted_numbers[-1] + 1),
    ])
    print()
    run_tests()