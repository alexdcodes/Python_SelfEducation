def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result


def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result


def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq
print search(seq, 34)

# PolyMorphism


def add(x, y):
    return x+y


print add(1, 2)
print add('Fish', 'license')
