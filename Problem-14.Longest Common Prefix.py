''' Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Initiate results
        res = "
        #Itereation using indexes through the first word of the list of words.
        for i in range(len(strs[0])):
            #Iteration through the rest of the strings
            for s in strs:
                #Here if the i equal to len of s or if the character at index i of the first word is not equal character at index of rest of the words return result.
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            #If the above algo is false, append the character at index i of word to res.
            res += s[i]
        # Return result
        return res
        
