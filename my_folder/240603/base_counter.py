def base_count(seq):
    data = dict()

    for base in seq:
        if base not in data:
            data[base] = 0
        data[base] += 1

    return data
