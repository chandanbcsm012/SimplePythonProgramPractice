def subarray_sum_indexes(arr, target):
    start, current_sum = 0, 0
    
    for end in range(len(arr)):
        current_sum += arr[end]

        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start+=1

        if current_sum == target:
            return [start, end]
    return -1
arr = [1, 2, 3, 7, 5]
target = 12
print(subarray_sum_indexes(arr, target))
