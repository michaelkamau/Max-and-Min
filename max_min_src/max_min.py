def find_max_min(values):
    res = set()
    min_v = min(values)
    max_v = max(values)
    res.add(min_v)
    res.add(max_v)
    return sorted(list(res))