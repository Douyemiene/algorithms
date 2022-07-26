def max_pdt_fast(numbers):
    indexOfFirst = 0
    indexOfSecond = 0
    length = len(numbers)
    for i in range(1, length):
        if numbers[indexOfFirst] < numbers[i]:
            indexOfFirst = i

    if indexOfFirst == 0:
        indexOfSecond = 1

    for j in range(0, length):
        if j != indexOfFirst and numbers[indexOfSecond] < numbers[j]:
            indexOfSecond = j

    return numbers[indexOfFirst] * numbers[indexOfSecond]


if __name__ == "__main__":
    print(max_pdt_fast([100000,90000]))


