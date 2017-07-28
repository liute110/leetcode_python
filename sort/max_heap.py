#coding=utf-8
'''
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
		heapify(nums,i,len(nums))

def heap_sort(nums):
	size  = len(nums) - 1
	build_heap(nums)
	for i in range(size,0,-1):
		nums[0],nums[i] = nums[i],nums[0]
		heapify(nums,0,i)

'''
'''
def heapify(nums,i,n):
	j = i * 2 + 1
	while j <= n:
		if j+1 <= n and nums[j+1] > nums[j]:
			j = j + 1
		if nums[i] > nums[j]:
			break 
		nums[i],nums[j] = nums[j],nums[i]
		i = j
		j = i * 2 + 1

def build_heap(nums):
	for i in range(len(nums)/2-1,-1,-1):
		heapify(nums,i,len(nums)-1)

def heap_sort(nums):
	build_heap(nums)
	print  nums
	for i in range(len(nums)-1,0,-1):
		nums[0],nums[i] = nums[i],nums[0]
		print i-1
		print nums[:i],nums[i:]
		heapify(nums,0,i-1)
		print nums[:i],nums[i:]
		print 
'''		


def heapify(num, start, end):
	j = start*2 + 1
	while j <= end:
		if(j+1 <= end and num[j+1]>num[j]):
			j = j+1
		if(num[start]>=num[j]):
			break
		num[start],num[j] = num[j],num[start]
		start = j;
		j = start*2 + 1;

def build_heap(num):
	for i in range(len(num)/2-1,-1,-1):
		heapify(num,i,len(num)-1)

def heap_sort(num):
	build_heap(num)
	for i in range(len(num)-1,-1,-1):
		nums[0],nums[i] = nums[i],nums[0]
		heapify(nums,0,i-1)




nums = [7,6,5,4,3]
heap_sort(nums)
print nums


nums = [3,4,5,6,7]
heap_sort(nums)
print nums

nums = [3,3,3,2,2,1,1,4,4]
heap_sort(nums)
print nums

nums = [3,3,3,-1,-1,-2,4,-1]
heap_sort(nums)
print nums