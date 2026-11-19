def selection_sort(data):
    a = data.copy()
    comparisons = swaps = 0
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1
    return a, comparisons, swaps

def insertion_sort(data):
    a = data.copy()
    comparisons = shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return a, comparisons, shifts

def bubble_sort(data):
    a = data.copy()
    comparisons = swaps = 0
    for i in range(len(a) - 1):
        changed = False
        for j in range(len(a) - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                changed = True
        if not changed:
            break
    return a, comparisons, swaps
# Негізгі (жеке нұсқа) тізім
values = [9, 9, 3, 12, 3, 1]
expected = sorted(values)
print("Бастапқы тізім:", values)
for fn in (selection_sort, insertion_sort, bubble_sort):
    result, comparisons, movements = fn(values)
    assert result == expected
    print(fn.__name__, result, comparisons, movements)
print("Бастапқы тізім өзгермеді:", values)

# Бес шекаралық тест
tests = [[], [7], [1, 2, 3], [3, 2, 1], [2, 1, 2, 1]]
for t in tests:
    for fn in (selection_sort, insertion_sort, bubble_sort):
        result, comparisons, movements = fn(t)
        assert result == sorted(t)
        print(t, fn.__name__, result, comparisons, movements)
print("Барлық тест сәтті өтті!")
