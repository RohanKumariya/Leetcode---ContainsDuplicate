''' Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"] '''

#Pretty simple O(n) solution.
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = Counter(words[0])
        for i in words:
            l = l & Counter(i)
        return l.elements()
        
