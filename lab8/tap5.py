# 5-тапсырма (қосымша). Қайталанатын элементтер
# Екілік іздеу бірінші кездесу индексін қайтаратындай өзгертілді

from task1_linear import linear_search, show_result
from task2_binary import binary_search


def binary_search_first(items, target):
    left, right = 0, len(items) - 1
    comparisons = 0
    result = -1
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if items[mid] == target:
            result = mid              # табылды, сол жақтан іздеуді жалғастыру
            right = mid - 1
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result, comparisons


if __name__ == "__main__":
    assert binary_search_first([1, 3, 3, 3, 5], 3)[0] == 1
    assert binary_search_first([], 3) == (-1, 0)
    repeated = [1, 3, 3, 3, 3, 3, 5]
    print("Тізім:", repeated, "| ізделетін мән: 3")
    show_result("Сызықтық", linear_search(repeated, 3))
    show_result("Екілік (қарапайым)", binary_search(repeated, 3))
    show_result("Екілік (бірінші кездесу)", binary_search_first(repeated, 3))