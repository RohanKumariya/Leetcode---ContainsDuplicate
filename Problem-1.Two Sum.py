''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2] ''' 

#Solution 1 - Using Hashmap
Class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Initializing Hashamp  
        prevMap = {}
        #Using enumerate to map index and num
        for ind, num in enumerate(nums):
            #Since there's exactly one solution this algorithm would help us find the other number if it is present in the Hashmap
            diff = target - num
            if diff in prevMap:
                #Returning both the indexes of the numbers
                return prevMap[diff], ind
            prevMap[num] = ind

        #If there's no solution we will return an empty list
        return []


# Solution 2 - Brute Force Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Initialize two loops to find the target number
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    #Returning indexes of both the numbers present
                    return i,j
