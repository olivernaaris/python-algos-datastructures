# Selection sort
# Algorithm average time complexity: Θ(n^2)

def selection_sort(arr):
    """
    Selection sort algorithm to sort a list of numbers using a marker that moves forward
    after each shift.

    """
    spot_marker = 0
    while spot_marker < len(arr):
        for num in range(spot_marker, len(arr)):
            if arr[num] < arr[spot_marker]:
                arr[spot_marker], arr[num] = arr[num], arr[spot_marker]
        spot_marker += 1
        print(arr)


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5] # original case
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1] # worst case
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # best case
selection_sort(l)
print(l)
