# Bubble sort
# Algorithm average time complexity: Θ(n^2)

def bubble_sort(arr):
    """
    Loops trough array elements and changes the position of array elements
    if left array element is bigger than the right one.
    Also, add 'swap_happened' variable to keep looping until no additional
    incorrectly sorted elements exist.
    """
    swap_happened = True
    while swap_happened:
        print("Bubble sort status: " + str(arr))
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5] # original case
# l = [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1] # worst case
# l = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10] # best case
bubble_sort(l)
