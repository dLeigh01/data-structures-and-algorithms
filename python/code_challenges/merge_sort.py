def merge_sort(nums):
	"""Sorts a list recursively in order from low to high through merge sorting
	"""
	length = len(nums)

	if length > 1:
		mid = int(length / 2)
		left = nums[:mid]
		right = nums[mid:]

		merge_sort(left)
		merge_sort(right)
		return merge(left, right, nums)

	return nums


def merge(left, right, nums):
	left_index = 0
	right_index = 0
	nums_index = 0

	while left_index < len(left) and right_index < len(right):
		if left[left_index] <= right[right_index]:
			nums[nums_index] = left[left_index]
			left_index += 1
		else:
			nums[nums_index] = right[right_index]
			right_index += 1

		nums_index += 1

	if left_index == len(left):
		nums[nums_index:] = right[right_index:]
	else:
		nums[nums_index:] = left[left_index:]

	return nums
