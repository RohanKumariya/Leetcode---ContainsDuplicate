''' Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0] ''' 

#Basic O(n) solution 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #Counting all the pre i values from the first index first.
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        #Counting all the post i values from the last index and multiplying all the values to result array of same index.
        post = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res

#Second Solution O(n) complexity. Passes 18/23 test cases.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i,j,l  = 0, 1, 0
        k = []
        pre = 1
        post = 1
        while i < len(nums):
            if i == 0:
                while j < len(nums):
                    post *= nums[j]
                    j += 1
                k.append(post)
                post = 1
            elif i > 0:
                j = i+1
                l = 0
                while j < len(nums):
                    post *= nums[j]
                    j += 1
                while l < i:
                    pre *= nums[l]
                    l += 1
                k.append(pre*post)
            post = 1
            pre = 1
            i += 1
        return k
