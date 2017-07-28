#coding=utf-8

def quick_sort(nums,low,high):
	if low < high:
		key_index = partition(nums,low,high)
		quick_sort(nums,low,key_index-1)
		quick_sort(nums,key_index+1,high)

def partition(nums,low,high):
	key = nums[low]
	while low < high:
		while low < high and nums[high] >= key: high -= 1
		nums[low] = nums[high]
		while low < high and nums[low] <= key: low += 1
		nums[high] = nums[low]
	nums[low] = key 
	return low

nums = [1]
quick_sort(nums,0,len(nums)-1)
print nums