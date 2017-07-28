#coding=utf-8

def heapify(nums,i,n):
	j = i * 2 + 1
	while j < n:
		if j+1 < n and nums[j] < nums[j+1]:
			j += 1
		if nums[i] > nums[j]:
			break 
		nums[i],nums[j] = nums[j],nums[i]
		i = j 
		j = i * 2 + 1

def build_heap(nums):
	for i in range(len(nums)/2-1,-1,-1):
		heapify(nums, i, len(nums))

def heap_sort(nums):
	build(nums)
	for i in range(len(nums)-1,0,-1):
		nums[i],nums[0] = nums[0],nums[i]
		heapify(nums,0,i)

nums = [4,2,6,1,9,-3,4,55,11,34,53,54,23,42,13]
heap_sort(nums)
print nums	
