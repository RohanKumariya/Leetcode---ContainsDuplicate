''' Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Initiate Hashmap
        hashmap = {}
        #Using enumerate to map index to nums[i]
        for i, v in enumerate(nums):
            #Algo to fill hashmap if nums[i] not present in hashmap
            if v not in hashmap:
                hashmap[v] = i
            #Algo to check if the condition is met else assigning a new index to the nums[i]
            else:
                if abs(i - hashmap[v]) >= k:
                    return True
                else:
                    hashmap[v] = i
