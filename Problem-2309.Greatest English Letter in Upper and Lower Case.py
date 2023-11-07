''' Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet.

Example 1:
Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

Example 2:
Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Example 3:
Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case. '''

#Basic O(n) solution with hashmaps:
class Solution:
    def greatestLetter(self, s: str) -> str:
        #Initialize result and uppercase and lowercase hashmaps 
        hashl = {}
        hashu = {}
        res = ""
        #Initialize loop for mapping characters in either of the hashmaps
        for i in s:
            if i not in hashl and i not in hashu:
                if i.islower():
                    hashl[i] = 1
                elif i.isupper():
                    hashu[i] = 1
        #This loop checks whether the uppercase characters are present based on the lowercase characters.
        for k, v in hashl.items():
            if k.upper() in hashu:
                #Changes result if the result is empty or the ordinal value of current character is greater than result.
                if not res:
                    res = k.upper()
                else:
                    if res < k.upper():
                        res = k.upper()
        #Return result
        return res
        
            
