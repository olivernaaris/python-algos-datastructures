# Insertion sort
# Algorithm average time complexity: Θ(n^2)

def insertion_sort(arr):
    """
    Insertion sort starts from index 1 and compares current index and previous index size.
    In case value in current index is smaller, we movie it back and compare with previous values until it's sorted.
    Once previous index values are sorted, we move the primary index forward.
    The secondary index is used to move back and sort previous values.
    """
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1


l = [6,1,8,4,10]
insertion_sort(l)
print(l)
