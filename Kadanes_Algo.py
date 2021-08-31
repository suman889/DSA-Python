'''
Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.

Input:
N = 5
Arr[] = {1,2,3,-2,5}
Output:
9
'''


class Solution:
  
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far =arr[0]
        curr_max = arr[0]
        
        for i in range(1,N):
            curr_max = max(arr[i], curr_max + arr[i])
            max_so_far = max(max_so_far,curr_max)
             
                
        return max_so_far
                
