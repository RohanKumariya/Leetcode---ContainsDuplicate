''' Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:

1 - Open brackets must be closed by the same type of brackets.
2 - Open brackets must be closed in the correct order.
3 - Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. '''

#This is a stack problem
class Solution:
    def isValid(self, s: str) -> bool:
        #Initializing stack and mapping all the closing paratheses to the opening ones
        stack = []
        closetoopen = {')':'(', '}': '{', ']':'['}
      
        #Initialize loop
        for char in s:
            if char in closetoopen:
                #This algorithm will help determine whether there are opening paratheses for all the closing ones
                if stack and stack[-1] == closetoopen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        #Return True if the stack is empty else False
        return True if not stack else False
