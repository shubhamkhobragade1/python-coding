class Solution:
    # brute force approach
    def solve(self, A, B):
        ln = len(A)
        left = A[:B]
        right = A[ln - B:]
        # print(right)
        ans = sum(left)
        for i in range(B):
            val1 = sum(left[:i])
            val2 = sum(right[i:])

            ans = max(ans, val1 + val2)
            # print(val1,val2,end=' ')

        return ans


class Solution:
    # using carray forward technique
    def solve(self, A, B):
        ln = len(A)

        ans = sum(A[:B])  # when we not take anything from last and complete left part
        # instutution: adding element  from right side and removing same element from start of right list
        # TC= o(B) and sc=o(1)
        temp1 = 0
        temp2 = sum(A[ln - B:])

        for i in range(B):
            ans = max(ans, temp1 + temp2)
            temp1 += A[i]
            temp2 -= A[ln - B + i]

        return ans


class Solution:
    # using prefix and suffix array
    def solve(self, A, B):
        ln = len(A)
        # TC=O(N) SC=O(N)
        ans = float('-inf') # bcoz constriant is # -10^3 <= A[i] <= 10^3 we cant use 0
        # ans =sum(A[:B])
        # instutution: adding element  from right side and removing same element from start of right list
        # TC= o(B) and sc=o(1)
        pre = [0] * (B + 1)
        suff = [0] * (B + 1)
        # A = [5, -2, 3 , 1, 2]
        # B = 3
        # pre=[0,5,3,6]
        # suff=[6,3,2,0]

        for i in range(1, B + 1):
            pre[i] = pre[i - 1] + A[i - 1]

        for i in range(B - 1, -1, -1):
            suff[i] = suff[i + 1] + A[ln - B + i]
        # print(suff)

        for i in range(B + 1):
            ans = max(ans, pre[i] + suff[i])

        return ans

# Q2. Pick from both sides!
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# You are given an integer array A of size N.
#
# You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
#
# Find and return the maximum possible sum of the elements that were removed after B operations.
#
# NOTE: Suppose B = 4, and array A contains 10 elements, then
#
# You can remove the first four elements or can remove the last four elements, or can remove 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can remove.
#
#
# Problem Constraints
# 1 <= N <= 10^5
#
# 1 <= B <= N
#
# -10^3 <= A[i] <= 10^3
#
#
#
# Input Format
# First argument is an integer array A.
#
# Second argument is an integer B.
#
#
#
# Output Format
# Return an integer denoting the maximum possible sum of elements you removed.
#
#
#
# Example Input
# Input 1:
#
#  A = [5, -2, 3 , 1, 2]
#  B = 3
# Input 2:
#
#  A = [ 2, 3, -1, 4, 2, 1 ]
#  B = 4