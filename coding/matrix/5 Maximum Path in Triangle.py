class Solution:# optimal solutions
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        # TC=O(N^2) SC=O(1)
        r=len(A)
        c=len(A[0])
        if r==1:
            return sum(A[0])

        for i in range(r-2,-1,-1):
            for j in range(i+1):# this is moving in trignle from bottom to top
                A[i][j]=A[i][j]+max(A[i+1][j],A[i+1][j+1])

        return A[0][0]
# Bruite force
# class Solution: #TC=O(N^2)*(2^N)  SC=O(N^2)
#     # @param A : list of list of integers
#     # @return an integer
#     def solve(self, A):
#
#         ln=len(A)
#         r=len(A)
#         c=len(A[0])
#         def recurse(i,j,m):
#             if i==r or j==c:
#                 return m
#             mx1=recurse(i+1,j,m+A[i][j])
#             mx2=recurse(i+1,j+1,m+A[i][j])
#
#             return max(mx1,mx2)
#
#         return recurse(0,0,0)






# Q5. Maximum Path in Triangle
# Solved
# Problem Description
#
# Given a 2D integer array A of size N * N representing a triangle of numbers.
#
# Find the maximum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# NOTE:
#
# Adjacent cells to cell (i,j) are only (i+1,j) and (i+1,j+1)
# Row i contains i integer and n-i zeroes for all i in [1,n] where zeroes represents empty cells.
#
#
# Problem Constraints
#
# 0 <= N <= 1000
#
# 0 <= A[i][j] <= 1000
#
#
#
# Input Format
#
# First and only argument is an 2D integer array A of size N * N.
#
#
#
# Output Format
#
# Return a single integer denoting the maximum path sum from top to bottom in the triangle.
#
#
#
# Example Input
#
# Input 1:
#
#  A = [
#         [3, 0, 0, 0]
#         [7, 4, 0, 0]
#         [2, 4, 6, 0]
#         [8, 5, 9, 3]
#      ]
# Input 2:
#
#  A = [
#         [8, 0, 0, 0]
#         [4, 4, 0, 0]
#         [2, 2, 6, 0]
#         [1, 1, 1, 1]
#      ]
#
#
# Example Output
#
# Output 1:
#
#  23
# Output 2:
#
#  19