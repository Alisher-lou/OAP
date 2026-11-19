# Жеке нұсқа 1. Студенттердің тест ұпайлары
# Орындаған: Нурлан Әлібек

from task1_linear import linear_search
from task2_binary import binary_search
from task3_compare import compare_table
from task5_repeat import binary_search_first

scores = [68, 92, 45, 76, 88, 54, 100, 73, 61, 85, 76, 49]
sorted_scores = sorted(scores)

print("Бастапқы тізім:", scores)
print("Сұрыпталған көшірме:", sorted_scores)
compare_table(scores, sorted_scores, [
    ("Берілген мән", 76),
    ("Бірінші элемент", scores[0]),
    ("Соңғы элемент", scores[-1]),
    ("Тізімде жоқ", 50),
])
print("Бос тізім: сызықтық", linear_search([], 76), "| екілік", binary_search([], 76))
print("76 ұпайы, екілік (бірінші кездесу):", binary_search_first(sorted_scores, 76))