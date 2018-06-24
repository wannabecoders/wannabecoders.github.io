def subset(n, acc, i, choices):
    if i == n:
        print(acc)
        return

    # put i in acc
    for choose in choices:
        if choose:
            acc.append(i)
            subset(n, acc, i+1, choices)
            acc.pop()
        else:
            subset(n, acc, i+1, choices)


subset(3, [], 0, [True, False])
