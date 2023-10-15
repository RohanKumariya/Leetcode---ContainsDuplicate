'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written from largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a Roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.'''

class Solution:
    def romanToInt(self, s: str) -> int:
        #Intializing the Hashsets
        hashset = {'I': 1, "V": 5, "X": 10, 'L': 50, 'C':100, "D": 500, 'M': 1000}
        hash2 = {'IV': 4, 'IX': 9, 'XL': 40, "XC":90, 'CD': 400, 'CM': 900}
        k = 0
        i = 0
      
        #Using the while loop to iterate through the Roman Number
        while i < len(s)-1:
            #This algo will figure out if the number is in Hash2 and add it to the num k.
            if s[i] + s[i+1] in hash2:
                #If i = length -2 the loop will break here and the the last two digits will be added to k
                if i == len(s)-2:
                    temp = s[i] + s[i+1]
                    k += hash2.get(temp)
                    break
                else:
                    temp = s[i] + s[i+1]
                    k += hash2.get(temp)
                    i += 2
                  
            #This else statement will add the numbers to k if the numbers are not in hash2. 
            else:
                k += hashset.get(s[i])
                i += 1
              
        #Here the last number would be added to k since the loop only runs to length of s-1 
        else:
            k += hashset.get(s[-1])

        #Return result
        return k
        
        
        
