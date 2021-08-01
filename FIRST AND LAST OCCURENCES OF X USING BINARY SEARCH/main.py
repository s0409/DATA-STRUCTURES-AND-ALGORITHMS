def first(nums, k):
    low = 0
    high = len(nums) - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            res = mid
            high = mid - 1
        elif nums[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

    return res


def last(nums, k):
    low = 0
    high = len(nums) - 1
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            res = mid
            low = mid + 1
        elif nums[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

    return res


def find(arr, n, x):
    # code here
    first_index = first(arr, x)
    last_index = last(arr, x)

    return first_index, last_index



arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
print(find(arr,n,x))


