class Solution:
    # TC=O(N) SC=O(N)
    def solve(self, A):
        ln=len(A)
        suff=[1]*ln
        suff[ln-1]=A[ln-1]
        pref=[1]*ln
        pref[0]=A[0]
        for i in range(1,ln): # this is fix conditions for suff array
            pref[i]=pref[i-1]*A[i]

        for i in range(ln-2,-1,-1): # this is fix conditions for suff array
            suff[i]=suff[i+1]*A[i]

        ans=[0]*ln
        for i in range(ln):
            if i==0:
                ans[i]=suff[1]
            elif i==ln-1:
                ans[i]=pref[ln-2]
            else:
                ans[i]=pref[i-1]*suff[i+1] # this is observations

        return ans


# Q4. Product array puzzle
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith element of the array.
#
# Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.
#
#
# Input Format
#
# The only argument given is the integer array A.
# Output Format
#
# Return the product array.
# Constraints
#
# 2 <= length of the array <= 1000
# 1 <= A[i] <= 10
# For Example
#
# Input 1:
#     A = [1, 2, 3, 4, 5]
# Output 1:
#     [120, 60, 40, 30, 24]
#
# Input 2:
#     A = [5, 1, 10, 1]
# Output 2:
#     [10, 50, 5, 50]