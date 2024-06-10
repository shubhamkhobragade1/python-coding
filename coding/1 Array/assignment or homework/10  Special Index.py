class Solution:
    # TC=SC=O(N)

    def solve(self, A):
        ans = 0
        ln = len(A)
        preOd = [0] * ln
        preEv = [0] * ln
        suffEv = [0] * ln
        suffOd = [0] * ln
        preEv[0] = A[0]
        suffEv[-1] = A[-1]

        for i in range(1, ln):
            if i % 2 == 0:
                preEv[i] = A[i] + preEv[i - 1]  # we r not doing -2 for getting last even of odd index
 # but doing -1 bcoz in this line if we already moved same elment at index -1 position which is at -2 positions
                preOd[i] = preOd[i - 1]
            else:
                preOd[i] = A[i] + preOd[i - 1]
                preEv[i] = preEv[i - 1]

        for i in range(ln - 2, -1, -1):
            if i % 2 == 0:
                suffEv[i] = suffEv[i + 1] + A[i]
                suffOd[i] = suffOd[i + 1]
            else:
                suffOd[i] = suffOd[i + 1] + A[i]
                suffEv[i] = suffEv[i + 1]

        # print(suffEv,suffOd)
        ans = 0
        for i in range(ln):
            if i == 0:
                if suffOd[i + 1] == suffEv[i + 1]:
                    ans+=1
            elif i == ln - 1:
                if preEv[i - 1] == preOd[i - 1]: # same if last index is not consider then previous index has sum
                    ans += 1
            else:# if index i removed then i-1 and i+1 is then sum but pre+suff combination since one index slide dowm
                if preEv[i - 1] + suffOd[i + 1] == preOd[i - 1] + suffEv[i + 1]:
                    ans += 1
        # print(ln)
        return ans

# Q1. Special Index
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
#
#
#
# Problem Constraints
# 1 <= n <= 105
# -105 <= A[i] <= 105
#
#
# Input Format
# First argument contains an array A of integers of size N
#
#
# Output Format
# Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
#
#
#
# Example Input
# Input 1:
# A=[2, 1, 6, 4]
# Input 2:
#
# A=[1, 1, 1]
#
#
# Example Output
# Output 1:
# 1
# Output 2:
#
# 3
#
#
# Example Explanation
# Explanation 1:
# Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
# Therefore, the required output is 1.
# Explanation 2:
#
# Removing arr[0] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Removing arr[1] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Removing arr[2] from the given array modifies arr[] to { 1, 1 } such that arr[0] = arr[1]
# Therefore, the required output is 3.