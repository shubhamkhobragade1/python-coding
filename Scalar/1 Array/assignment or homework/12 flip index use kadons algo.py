class Solution: # this is brute force where TC=O(N^2)
    # institution: calculate sum of all '1' at start then in given subarray/range count 0 and 1
    # since we r fliping then use count of 0 as 1 and viseverse, so in that range we add count and
    # 0 which act as count of 1 and remove prevously added 1 since it bcoz 0
    def flip(self, A):
        ans=()
        ln=len(A)
        prev=0
        start_c=A.count('1')
        for l in range(ln):
            # temp=start_c
            for r in range(l+1,ln+1):
                # for r in range(1,l+1):
                co_0=A[l:r].count('0')
                co_1=A[l:r].count('1')
                curr_count=co_0-co_1+start_c
                if curr_count>start_c and prev<curr_count:
                    ans=(l+1,r)
                    prev=curr_count
                    # print(ans,curr_count,end=' ')


        return ans
class Solution1: # tc=o(n) sc=o(n) class Solution1:# this is optimal solution with TC=O(N)

    def flip(self, A):

        ln = len(A)
        kadon = [0] * ln
        for i in range(ln): #'0101100'
            if A[i] == '1':
                kadon[i] = -1
            else:
                kadon[i] = 1

        curr = prev_best = 0 #= [1,-1,1,-1,-1,1,1]
        next_left_can_becm = i = 0
        r = -1
        for i in range(ln):
            curr += kadon[i]
            if curr < 0:
                curr = 0
                next_left_can_becm = i + 1
            elif curr > prev_best:
                prev_best = curr
                r = i
                l = next_left_can_becm

        if r == -1:
            return ()
        else:
            return (l + 1, r + 1)


# Q2. Flip
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.
#
# Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
#
# If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
#
# NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
#
#
#
# Problem Constraints
# 1 <= size of string <= 100000
#
#
#
# Input Format
# First and only argument is a string A.
#
#
#
# Output Format
# Return an array of integers denoting the answer.
#
#
#
# Example Input
# Input 1:
#
# A = "010"
# Input 2:
#
# A = "111"
#
#
# Example Output
# Output 1:
#
# [1, 1]
# Output 2:
#
# []
#
#
# Example Explanation
# Explanation 1:
#
# A = "010"
#
# Pair of [L, R] | Final string
# _______________|_____________
# [1 1]          | "110"
# [1 2]          | "100"
# [1 3]          | "101"
# [2 2]          | "000"
# [2 3]          | "001"
#
# We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
# Explanation 2:
#
# No operation can give us more than three 1s in final string. So, we return empty array [].