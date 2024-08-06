def binary_search(arr, target):
    left = arr[0]
    right = len(arr)-1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        else: 
            if left < target:
                return left + 1