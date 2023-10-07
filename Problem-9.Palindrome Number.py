''' Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. '''

#Easy solution by converting the Integer to a list and reversing it to find whether its palindrome or not.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        return x == x[::-1]
