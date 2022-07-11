def minOps(index, n, computed):
    if index <= 1:
        if index == n:
            return 0
        computed[index] = 0
        return minOps( index + 1, n, computed)

    elif index <= 3:
        if index == n:
            return 1

        computed[index] = 1
        return minOps( index + 1, n, computed)
    # unsure
    elif index == n + 1:
        return computed[n]

    nOverTwo = index // 2
    nModuloTwo = index % 2
    nOverThree = index // 3
    nModuloThree = index % 3

    if nModuloTwo <= 3:
        forTwo = computed[nOverTwo] + 1 + nModuloTwo
    else:
        forTwo = computed[nOverTwo] + 1 + computed[nModuloTwo]

    if nModuloThree <= 3:
        forThree = computed[nOverThree] + 1 + nModuloThree
    else:
        forThree = computed[nOverThree] + 1 + computed[nModuloThree]

    computed[index] = min(forTwo, forThree)

    return minOps( index + 1, n, computed )

    




n = 10
computed = [0] * ( n + 1)
print(minOps( 0, n, computed ))