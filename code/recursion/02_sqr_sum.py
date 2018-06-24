def sqr_sum(n):
    if n == 0:
        return 0
    return n**2 + sqr_sum(n-1)

# 1^2 + 2^2 + 3^2 = 14
print(sqr_sum(3))
