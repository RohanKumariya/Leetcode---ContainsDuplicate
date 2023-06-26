'''Problem - 242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

'SOLUTION - 1 (HARD CODED)'
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # First we'll check if the length of both the strings are same. If not we immediately return False because then it cannot be a valid anagram. 
      if len(s) != len(t):
        return false
      # If the length of the strings is same we'll initialize 2 hashmaps for both strings to count the number of occurrences of characters in each string.
      hashmapS, hashmapT = {}, {}

      # Populating HashmapS
      for i in s:
        if i not in hashmapS:
          hashmapS[i] = 0
        hashmapS[i] += 1

      # Populating HashmapT
      for j in t:
        if j not in hashmapT:
          hashmapT[j] = 0
        hashmapT[j] += 1

      #Then we'll return whether both hashmaps are equal or not. If they're equal it's a valid anagram
      return hashmapS == hashmapT

'SOLUTION - 2 (SOFT CODED)'
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # We know that both strings need to be the same. We can use Sorted(built in function) for one line code and return values.
      return sorted(s) == sorted(t)

'SOLUTION - 3 (SOFT CODED)'
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # Similar to solution 2 we can also use Counter function which will give us no. of occurences of each character same as solution 1 in just one line.
      return Counter(s) == Counter(t)
