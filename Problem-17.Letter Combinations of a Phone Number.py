'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"] '''

#O(n) time complexity solution with hashmap.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Intitalize hashmap and map all the numbers to the given alphabets 
        hashmap = {'2':'abc', '3':'def', 4:'ghi', '5':'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        #Intitialize the result combinations
        combinations = [""]
        #If digits string is empty return empty string
        if digits == '':
            return ""
        #Initialze first loop to go through each numbers.
        for num in digits:
            #Through hashmap.get() method get all the characters mapped to the number and initialze new combination.
            characters = hashmap.get(num)
            new_combination = []
            #Loop through each character of each number.
            for char in characters:
                #Loop thorugh combinations to append new combinations to the result.
                for combo in combinations:
                    new_combination.append(combo+char)
            combinations = new_combination
        #Return result of all the combinations
        return combinations
