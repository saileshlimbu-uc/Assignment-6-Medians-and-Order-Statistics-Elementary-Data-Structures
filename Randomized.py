import random

# Helper function to partition the array around the pivot for quickselect
def quickselect_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot_value = arr[high]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

# Quickselect to find the k-th smallest element
def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = quickselect_partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

# Randomized algorithm to select the k-th smallest element
def randomized_select(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k - 1)
