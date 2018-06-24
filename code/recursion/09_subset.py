def subset(n, acc, i):
    if i == n:
        print(acc)
        return

    # put i in acc
    acc.append(i)
    subset(n, acc, i+1)
    acc.pop()

    # don't put i in acc
    subset(n, acc, i+1)

subset(3, [], 0)
