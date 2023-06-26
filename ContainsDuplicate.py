'''Problem 217 - Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1: Input: nums = [1,2,3,1]
	   Output: True
Example 2: Input: nums = [1,2,3,4]
   	   Output: false'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #Initialize a hashset to find distinct values
	hashset = set()

	#Initializing the loop for finding distinct Values
	for i in nums:
		
		#Condition to check whether the number is already in the list if it is we return True
		if i in hashset:
			return True
			
		#If the value is distinct and not present in the list. We add the number to the hashset
		hashset.add(i)

	#If all values are unique we return False.
	return False
