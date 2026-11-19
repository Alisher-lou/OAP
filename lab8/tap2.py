# 2-тапсырма. Екілік іздеу
# Тізімнің сұрыпталған көшірмесінде екілік іздеу орындалады

from task1_linear import read_numbers, read_target, show_result


def binary_search(items, target):
    """Екілік іздеу; items өсу ретімен сұрыпталған болуы тиіс."""
    left, right = 0, len(items) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if items[mid] == target:
            return mid, comparisons
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


if __name__ == "__main__":
    numbers = read_numbers(10)
    target = read_target()
    sorted_numbers = sorted(numbers)          # бастапқы тізім өзгермейді
    print("Бастапқы тізім:", numbers)
    print("Сұрыпталған көшірме:", sorted_numbers)
    show_result("Екілік іздеу", binary_search(sorted_numbers, target))