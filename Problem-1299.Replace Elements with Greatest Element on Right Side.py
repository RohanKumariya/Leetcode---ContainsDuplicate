''' Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

Example 2:
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0. '''

#Basic O(n^2). Algorithm could be better.
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #Initialize the initial max
        max_num = max(arr)
        #Loop through the array.
        for i in range(len(arr)):
            #If i reaches the last position of the array then change the last value of the array to -1 and break loop
            if i == len(arr)-1:
                arr[i] = -1
                break
            #If the value of array at index i is not the greater than the next max value convert all the values to the upcoming max value. 
            if arr[i] != max_num:
                arr[i] = max_num
            #Else look for the next max value and convert the value at index i to max value
            else:
                max_num = max(arr[i+1:len(arr)])
                arr[i] = max_num
        #Return result 
        return arr
