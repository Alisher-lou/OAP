# 4-тапсырма. Салыстыру санының деректер көлеміне тәуелділігі
# Өлшемі 10, 100, 1000 реттелген тізімдерде соңғы элемент және жоқ мән ізделеді

from task1_linear import linear_search
from task2_binary import binary_search

print(f"{'n':>5}  {'Соңғы: сыз.':>12}{'Соңғы: екіл.':>14}{'Жоқ: сыз.':>11}{'Жоқ: екіл.':>12}")
for size in [10, 100, 1000]:
    data = list(range(size))                  # 0, 1, ..., size-1
    last = size - 1                           # соңғы элемент
    missing = size                            # тізімде жоқ мән
    print(f"{size:>5}  {linear_search(data, last)[1]:>12}{binary_search(data, last)[1]:>14}"
          f"{linear_search(data, missing)[1]:>11}{binary_search(data, missing)[1]:>12}")