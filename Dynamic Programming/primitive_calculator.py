import sys

# recursion isn't always the best way to solve a problem.
sys.setrecursionlimit(10000)

def minOps(index, n, computed):
    global ans
    global calculations
    if index <= 1:
        if index == n:
            return 0
        computed[index] = 0
        calculations[index] = [index]
        return minOps( index + 1, n, computed)

    elif index <= 3:
        if index == n:
            return 1

        computed[index] = 1
        calculations[index] = [index]
        return minOps( index + 1, n, computed)
    # unsure
    elif index == n + 1:
        return computed[n]

    nOverTwo = index // 2
    nModuloTwo = index % 2
    nOverThree = index // 3
    nModuloThree = index % 3

    c1 = []
    c2 = []
    if nModuloTwo <= 3:
        forTwo = computed[nOverTwo] + 1 + nModuloTwo
        if calculations[nOverTwo] == [1]:
            c1 = [ calculations[nOverTwo][-1] * 2]
        else:
            c1 = calculations[nOverTwo] + [ calculations[nOverTwo][-1] * 2]
        for i in range(1, nModuloTwo + 1):
            c1.append( c1[-1] + 1  )
    else:
        forTwo = computed[nOverTwo] + 1 + computed[nModuloTwo]
        c1 = calculations[nOverTwo] + calculations[nModuloTwo]

    if nModuloThree <= 3:
        forThree = computed[nOverThree] + 1 + nModuloThree
        if calculations[nOverThree] == [1]:
            c2 = [ calculations[nOverThree][-1] * 3]
        else:
            c2 = calculations[nOverThree] + [ calculations[nOverThree][-1] * 3]
        for i in range(1, nModuloThree + 1):
            c2.append( c2[-1] + 1  )
    else:
        forThree = computed[nOverThree] + 1 + computed[nModuloThree]
        c2 = calculations[nOverThree] + calculations[nModuloThree]


    if forTwo <= forThree:
        calculations[index] = c1
    else:
        calculations[index] = c2
        

    computed[index] = min(forTwo, forThree)
    
    return minOps( index + 1, n, computed )



input = sys.stdin.read()
n = int(input)
calculations = [ 0 ] * ( n + 1 )
computed = [0] * ( n + 1)
ans = [1]

print(minOps( 0, n, computed ))
calculations[n].insert(0, 1)
for i in calculations[n]:
    print(i, end=" ")
print('')
