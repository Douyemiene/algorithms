def triplet_with_smaller_sum(arr, target):
    triplets = []
    arr.sort()  

    for i, first in enumerate(arr): 
        target_without_first = target - first 
        j = i + 1 
        k = len(arr) - 1

        while j < k:
            second_plus_third = arr[j] + arr[k]

            if second_plus_third < target_without_first: 
                triplets.append([arr[i], arr[j], arr[k]])

            k = k - 1

    return triplets


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
