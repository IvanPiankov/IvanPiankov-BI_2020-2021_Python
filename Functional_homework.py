import itertools

def generate(n):
    for _ in range(1, n+1):
        iter = itertools.combinations_with_replacement("ACTG", _)
        for each in iter:
            yield("".join(str(_) for _ in each))

print(list(generate(3)))
