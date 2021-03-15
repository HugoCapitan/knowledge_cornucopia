
# This method assumes that l < r
def partition(arr, l, r):
    i = l - 1
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1

def quicksort(arr, l, r):
    if l < r:
        partition_index = partition(arr, l, r)

        quicksort(arr, l, partition_index)
        quicksort(arr, partition_index + 1, r)

        


                

