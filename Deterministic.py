import math

# Helper function to partition the array around a pivot
def partition(arr, low, high, pivot):
    pivot_val = arr[pivot]
    arr[high], arr[pivot] = arr[pivot], arr[high]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_val:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

# Deterministic median of medians function to find the median
def median_of_medians(arr, low, high, k):
    if low == high:
        return arr[low]

    # Divide array into groups of 5 and find their medians
    medians = []
    for i in range(low, high + 1, 5):
        group = sorted(arr[i:i + 5])
        medians.append(group[len(group) // 2])

    # Recursively find the median of the medians
    median = median_of_medians(medians, 0, len(medians) - 1, len(medians) // 2)

    # Partition the array around the median
    pivot_index = arr.index(median)
    partition_index = partition(arr, low, high, pivot_index)

    if k == partition_index:
        return arr[k]
    elif k < partition_index:
        return median_of_medians(arr, low, partition_index - 1, k)
    else:
        return median_of_medians(arr, partition_index + 1, high, k)

# Find the k-th smallest element using median of medians
def deterministic_select(arr, k):
    return median_of_medians(arr, 0, len(arr) - 1, k - 1)
