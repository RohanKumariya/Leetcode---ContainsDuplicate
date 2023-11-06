''' You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container. 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1 '''

#Basic O(n) solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Initializing the breadth of the container and the pointers i, j
        breadth = len(height)-1
        i, j = 0, len(height)-1
        #This is the maximum amount of water the container can hold.
        max_wat = 0
        #Initialize the loop so that it doens't cross each other
        while i < j:
            #This algo will determine whether the the max water the container is holding.
            if height[i] > 0 and height[j] > 0:
                #If the left poiner value is less than the right pointer value it moves the left pointer to the right else move right pointer to left.
                if height[i] <= height[j]:
                    area = height[i] * breadth
                    max_wat = max(max_wat, area)
                    i += 1
                elif height[j] < height[i]:
                    area = height[j] * breadth
                    max_wat = max(max_wat, area)
                    j -= 1
            #If the height at either pointer is 0 move the pointer.
            else:
                if height[i] == 0:
                    i += 1
                else:
                    j -= 1
            #Decrease breadth whenever either pointer moves
            breadth -= 1
        #Returning the maximum water the cointer can hold.
        return max_wat
