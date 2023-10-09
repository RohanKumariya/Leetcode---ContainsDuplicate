''' Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
In the American keyboard:
- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm". 

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []
'''

#This solution is O(n^2) complexity where the loop runs twice for each character of each word.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
      
        ans = []

        #Iteration of first loop where the loop iterates through each word
        for word in words:
            flag = 0
            temp = word
            word = word.lower()

            #This algo will figure out which row could be the word in by the first character of the word
            if word[0] in row1:
                res_row = row1
            elif word[0] in row2:
                res_row = row2  
            elif word[0] in row3:
                res_row = row3
            
            #This loop will iterate through each character and will figure out whether all characters are in the same row or not.
            for i in word:
                if i not in res_row:
                    flag = 1
                    break
                  
            #If all the characters are in the same row, append the temp word to ans and return answer
            if flag == 0:
                ans.append(temp)
        return ans
            
