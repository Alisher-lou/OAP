def count_by_sign(values):
    positive = negative = zeros = even = odd = 0
    for value in values:
        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            zeros += 1
        if value % 2 == 0:               # 0 % 2 == 0, сондықтан 0 жұп сан
            even += 1
        else:
            odd += 1
    return positive, negative, zeros, even, odd