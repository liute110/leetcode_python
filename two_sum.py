#coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_nums = sorted(nums)
        low = 0
        high = len(new_nums) - 1
        result = []
        while low  < high:
            data = new_nums[low] + new_nums[high]
            if data == target:
                for i in range(len(nums)):
                    if nums[i] == new_nums[low] or nums[i] == new_nums[high]:
                        result.append(i)
                break
            elif data > target:
                high -= 1
            else:
                low += 1
        return result
                
