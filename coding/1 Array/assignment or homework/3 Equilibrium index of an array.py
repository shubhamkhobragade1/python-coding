class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, arr):
        for i in range(1,len(arr)):
            arr[i]=arr[i-1]+arr[i]

        INF=float('inf')
        ans=INF
        ln=len(arr)
        # print(arr)
        for i in range(0,ln):
            if i>0:# here for i==0 we need to assign val=0 and right sum will get calculate
                val=arr[i-1]
            else:
                val=0
            if val==(arr[ln-1]-arr[i]): # last element will get consider as loop move upto ln
            # just we was doing i-1 so puted extrac conditions
                ans=min(ans,i)

        return ans if ans!=INF else -1

# Q2. Equilibrium index of an array
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# You are given an array A of integers of size N.
#
# Your task is to find the equilibrium index of the given array
#
# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
#
# If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.
#
# Note:
#
# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.
#
#
# Problem Constraints
# 1 <= N <= 105
# -105 <= A[i] <= 105
#
#
# Input Format
# First arugment is an array A .
#
#
# Output Format
# Return the equilibrium index of the given array. If no such index is found then return -1.
#
#
# Example Input
# Input 1:
# A = [-7, 1, 5, 2, -4, 3, 0]
# Input 2:
#
# A = [1, 2, 3]
#
#
# Example Output
# Output 1:
# 3
# Output 2:
#
# -1