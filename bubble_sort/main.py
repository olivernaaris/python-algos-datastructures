def bubble_sort(arr):
    for num in range(len(arr)-1):
        if arr[num] > arr[num+1]:
            print("Swap happened")
            arr[num], arr[num+1] = arr[num+1], arr[num]
            print(arr)


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)

