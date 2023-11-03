''' Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself. 

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true ''' 

#Basic O(n) solution
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize hashmaps for both the strings 
        hashs = {}
        hasht = {}
        #Looping throught the first string to map it to the one character returning false if it isn't the same as the mapped character.
        for i in range(len(s)):
            if s[i] not in hashs:
                hashs[s[i]] = t[i]
            if t[i] != hashs.get(s[i]):
                return False
        #Looping through the second string to map the character
        for i in range(len(t)):
            if t[i] not in hasht:
                hasht[t[i]] = s[i]
        #Returing whether the length of both the hashmaps are same.
        return len(hashs) == len(hasht)

        
