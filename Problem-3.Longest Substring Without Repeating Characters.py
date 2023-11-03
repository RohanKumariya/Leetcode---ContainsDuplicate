''' Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. ''' 

#Basic O(n) solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Initialize max length.
        max_len = 0
        #Initialize left pointer and set which will determine the distinct characters.
        char_set = set()
        l = 0
        #Looping through string s
        for r in range(len(s)):
            #Using while loop to determine whether the char is in the set and removing if present.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            #Adding the character to set if not present
            char_set.add(s[r])
            max_len = max(max_len, r-l +1)
        #Returning the maximum length of the substring
        return max_len
