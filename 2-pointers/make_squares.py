def make_squares(arr):
    arr_length = len(arr)
    left = 0
    right = arr_length - 1
    squares = [0 for x in range(arr_length)]
    current_index = arr_length - 1

    while current_index > 0:
        sqr_left_pointer_element = arr[left] ** 2
        sqr_right_pointer_element = arr[right] ** 2

        if sqr_left_pointer_element >= sqr_right_pointer_element:
            squares[current_index] = sqr_left_pointer_element 
            left += 1
        else:
            squares[current_index] = sqr_right_pointer_element
            right -= 1

        current_index -= 1

    return squares


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()

