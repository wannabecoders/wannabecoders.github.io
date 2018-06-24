def permutate(n, acc, choices):
    if len(acc) == n:
        print(acc)
        return

    for i, choose in enumerate(choices):
        if choose: 
            choices[i] = False
            acc.append(i)
            permutate(n, acc, choices)
            choices[i] = True
            acc.pop()

permutate(3, [], [True] * 3)
