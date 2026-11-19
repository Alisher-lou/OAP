def is_passed(score):
    if score < 0 or score > 100:
        return None                       # диапазоннан тыс балл
    return score >= 50