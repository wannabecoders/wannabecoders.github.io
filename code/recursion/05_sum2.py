def sum(n, acc):
    if n == 0:
        return acc
    return sum(n - 1, acc + n)

print(sum(100, 0))
