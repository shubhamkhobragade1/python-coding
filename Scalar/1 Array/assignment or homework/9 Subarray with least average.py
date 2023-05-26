class Solution:
    # TC=O(N)
    def solve(self, A, B):
        val = float('inf')
        temp = sum(A[:B])
        ln = len(A)
        if temp / B < val:
            ans = 0
            val = temp / B
        vv = int(10 ** 5)
        # print(vv)

        for i in range(B, ln):

            temp += A[i] - A[i - B]  # Sliding window which add next and prev
            if temp / B < val:
                ans = i - B + 1  # this is start index of window
                val = temp / B

        return ans


# Q3. Subarray with least average
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# Given an array of size N, find the subarray of size K with the least average.
#
#
#
# Problem Constraints
# 1<=k<=N<=1e5
# -1e5<=A[i]<=1e5
#
#
# Input Format
# First argument contains an array A of integers of size N.
# Second argument contains integer k.
#
#
# Output Format
# Return the index of the first element of the subarray of size k that has least average.
# Array indexing starts from 0.
#
#
# Example Input
# Input 1:
# A=[3, 7, 90, 20, 10, 50, 40]
# B=3
# Input 2:
#
# A=[3, 7, 5, 20, -10, 0, 12]
# B=2
#
#
# Example Output
# Output 1:
# 3
# Output 2:
#
# 4
#
#
# Example Explanation
# Explanation 1:
# Subarray between indexes 3 and 5
# The subarray {20, 10, 50} has the least average
# among all subarrays of size 3.
# Explanation 2:
#
#  Subarray between [4, 5] has minimum average