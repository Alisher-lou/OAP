def transform(values):
    squares = []
    positive_even = []
    for value in values:                 # бастапқы тізім өзгермейді
        squares.append(value ** 2)
        if value > 0 and value % 2 == 0:
            positive_even.append(value)
    return squares, positive_even