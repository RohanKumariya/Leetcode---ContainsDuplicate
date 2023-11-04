'''Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2] '''

#Basic O(n) solution with hashmap.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #Initialize hashmap and the result array.
        hashmap = {}
        res = []
        #Populating the hashmap with occurence count of the characters.
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        #Loop through the hashmap to get which keys that have appeared more than len(nums)/3 times and appending to result array
        for k,v in hashmap.items():
            if v > len(nums)/3:
                res.append(k)
        #Returning result array
        return res
        
        
        
