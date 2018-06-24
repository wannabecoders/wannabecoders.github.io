def sqr_sum(n, acc):
    if n == 0:
        return acc
    return sqr_sum(n - 1, acc + n**2)

# 1^2 + 2^2 + 3^2 = 14
print(sqr_sum(3, 0))
