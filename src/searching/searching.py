def linear_search(arr, target):
    for i, elem in enumerate(arr):
        if elem == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start_idx = 0
    end_idx = len(arr) - 1
    
    try: arr[end_idx]
    except: return -1 # length of arr is zero

    midpoint = len(arr) // 2
    while start_idx != end_idx:
        if arr[midpoint] == target:
            return midpoint
        elif target > arr[midpoint]:
            # use upper half of sub_arr
            start_idx = midpoint + 1 # (end_idx does not change)
        elif target < arr[midpoint]:
            # use lower half of sub_arr
            end_idx = midpoint - 1 # (start_idx does not change)
        midpoint = start_idx + (end_idx - start_idx)//2

    if target == arr[start_idx]:
        return start_idx
    else:
        return -1  # not found
