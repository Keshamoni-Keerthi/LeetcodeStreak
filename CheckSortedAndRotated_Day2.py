'''
1752. CHECK IF ARRAY IS SORTED AND ROTATED
Given an array nums, return true if the array was originally
sorted in non-decreasing order, then rotated some number of
positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B
of the same length such that A[i] == B[(i+x) % A.length],
where % is the modulo operation.
'''
class Solution(object):
    def check(self, nums):
        count=1
        for i in range(1,len(nums)*2):
            if nums[(i-1)%len(nums)]<=nums[i%len(nums)]:
                count+=1
            else:
                count=1
            if count==len(nums):
                return True
        return len(nums)==1
