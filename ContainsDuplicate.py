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

	#If all values are unique we return False
	return False
			
				
        
