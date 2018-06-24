## Function is the container of procedures

## What's continuation
def add(x, y, cont):
    return cont(x + y)

print("1 + 2 =", add(1, 2, lambda _: _))

def mul(x, y, cont):
    return cont(x * y)

print("2 * 3 + 4 =", mul(2, 3,
    lambda _: add(_, 4, lambda _: _)))

# sum in continuation passing style(CPS)
def sum(n, cont):
    if n == 0:
        return cont(0)

    return sum(n - 1, lambda _: cont(_ + n))

# invariant: the input of `cont` is the result of sum(n)
print("sum(10) =", sum(10, lambda _: _))
