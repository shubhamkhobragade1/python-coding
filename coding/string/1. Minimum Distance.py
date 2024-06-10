class Solution:
    # @param A : string
    # @return an integer
    # TC=O(N) SC=O(1)
    def solve(self, A):
        if 'o' not in A:
            return -1
        INF=float('inf')
        mn=INF
        x,o=-1,-1
        for i in range(len(A)):
            if A[i]=='o':
                o=i
            if A[i]=='x':
                x=i
            if x!=-1 and o!=-1:
                val=abs(x-o)
                if mn>val:
                    mn=val
        return mn if mn!=INF else -1


# Q1. Minimum Distance
# Solved
# Problem Description
#
# Given a string A which contains only three characters {'x', 'o', '.'}.
#
# Find minimum possible distance between any pair of 'x' and 'o' in the string.
#
# Distance is defined as the absolute difference between the index of 'x' and 'o'.
#
# NOTE: If there is no such pair return -1.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 105
#
#
#
# Input Format
#
# First and only argument is a string A.
#
#
#
# Output Format
#
# Return an integer denoting the minimum possible distance.
#
#
#
# Example Input
#
# Input 1:
#
#  A = "x...o.x...o"
# Input 2:
#
#  A = "xxx...xxx"
#
#
# Example Output
#
# Output 1:
#
#  2
# Output 2:
#
#  -1