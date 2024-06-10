class Solution:
    # @param A : string
    # @return an integer
    # TC=SC=O(N)
    # institution: just append same string back, find same index if got increase both value and set in lps
    # otherwise start from second index value -1 in not 0
    def solve(self, A):
        val = self.create_lps(A[::-1] + '$' + A)
        return len(A) - val

    def create_lps(self, A):
        ln = len(A)
        lps = []  # longest prefix suffix length
        i, j = 1, 0
        lps = [0] * ln
        lps[0] = j

        while (i < ln):
            if A[i] == A[j]:  # if same we r moving from that indes ahead
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    # lps[i]=0 # this below 3 lines also works whithout if part
                    i += 1
                    j = 0
        print(lps)
        return lps[-1]  # maximum value in this lps is the longest palindrome in string

# brute force  TC=O(N^2) here we r instead of adding at end we r removing from start by neglecting
# in use and check if it is palindrome
# class Solution:
#     # @param A : string
#     # @return an integer
#     def solve(self, A):
#         res = 0
#         ln=len(A)
#
#         for i in range(ln):
#             if A[i:] == A[i:][::-1]:
#                 return res
#             res+=1
#
#         return res


# Q4. Minimum Appends for Palindrome!
# Solved
# Problem Description
#
# Given a string A consisting of lowercase characters.
#
# We need to tell minimum characters to be appended (insertion at end) to make the string A a palindrome.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 105
#
# A consists only of lower-case characters.
#
#
#
# Input Format
#
# First argument is an string A.
#
#
#
# Output Format
#
# Return a integer denoting the minimum characters to be appended (insertion at end) to make the string A a palindrome.
#
#
#
# Example Input
#
# Input 1:
#
#  A = "abede"
# Input 2:
#
#  A = "aabb"
#
#
# Example Output
#
# Output 1:
#
#  2
# Output 2:
#
#  2
#
#
# Example Explanation
#
# Explanation 1:
#
#  We can make string palindrome as "abedeba" by adding ba at the end of the string.