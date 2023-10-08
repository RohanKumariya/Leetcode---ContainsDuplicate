'''Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1] '''

#Similar to Pascal Triangle this is O(n^2) time complexity
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        #Similar to the previous Pascal triangle iteration through the loop, however, the array at rowIndex needs to be returned so we'll go through until the end since this question considers 0th index as well
        for i in range(rowIndex):
            temp = [0] + res[-1] + [0]
            row = []
            #Iterating through 2nd loop to build the Pascal triangle
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        #The difference in this question is that the result would be the last index of the result array since rowIndex = res[-1]
        return res[-1]

