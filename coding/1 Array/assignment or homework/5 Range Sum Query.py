class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an list of long
    def rangeSum(self, A, B):
        ln = len(A)
        for i in range(1, ln):
            A[i] = A[i - 1] + A[i]

        ans = []
        for i, j in B:
            if i != 0:
                val = A[j] - A[i - 1]
            else:
                val = A[j]
            ans.append(val)

        return ans

# Q1. Range Sum Query
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
#
#
#
# Problem Constraints
# 1 <= N, M <= 105
# 1 <= A[i] <= 109
# 0 <= L <= R < N
#
#
# Input Format
# The first argument is the integer array A.
# The second argument is the 2D integer array B.
#
#
# Output Format
# Return an integer array of length M where ith element is the answer for ith query in B.
#
#
# Example Input
# Input 1:
# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]
# Input 2:
#
# A = [2, 2, 2]
# B = [[0, 0], [1, 2]]
#
#
# Example Output
# Output 1:
# [10, 5]
# Output 2:
#
# [2, 4]