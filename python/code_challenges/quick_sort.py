def quick_sort(nums, left, right):
    """Sorts a list in ascending order through quick sort
    """
    if left < right:
        position = partition(nums, left, right)
        quick_sort(nums, left, position - 1)
        quick_sort(nums, position + 1, right)
    return nums


def partition(nums, left, right):
    pivot = nums[right]
    low = left - 1
    for i in range(left, right):
        if nums[i] <= pivot:
            low += 1
            swap(nums, i, low)

    swap(nums, right, low + 1)
    return low + 1


def swap(nums, i, low):
    temp = nums[i]
    nums[i] = nums[low]
    nums[low] = temp
    return nums
