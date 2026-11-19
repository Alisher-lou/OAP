def list_sum(values):
    total = 0
    for value in values:
        total += value
    return total


def list_average(values):
    if not values:                       # бос тізім: нөлге бөлуден сақтану
        return None
    return list_sum(values) / len(values)