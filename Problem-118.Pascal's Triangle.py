''' Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown: 

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]] '''

#Pretty Basic O(n^2) complexity solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #Initialize the base case
        res = [[1]]

        #Iterating through 1st loop to create the required number of lists 
        for i in range(numRows-1):
            #Temporary list for the addition of the pointers
            temp = [0] + res[-1] + [0]
            row = []
            #Iterating through 2nd loop to build the Pascal triangle
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j + 1])
            #Append the final row to the result
            res.append(row)
        return res
      
