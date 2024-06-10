class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # TC=O(A^(0.5))
        # sc=o(1)
        ans = 0
        i = 1
        while (i * i <= A):
            if A % i == 0 and i != A // i:  # here when i (first factor and A//i second factor r equal we need to count only once)
                ans += 2

            elif A % i == 0:
                ans += 1
            i += 1

        return ans




# Q2. Count Factors - 2
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# Given an integer A, you need to find the count of it's factors.
#
# Factor of a number is the number which divides it perfectly leaving no remainder.
#
# Example : 1, 2, 3, 6 are factors of 6
#
#
# Problem Constraints
# 1 <= A <= 109
#
#
# Input Format
# First and only argument is an integer A.
#
#
# Output Format
# Return the count of factors of A.
#
#
# Example Input
# Input 1:
# 5
# Input 2:
# 10
#
#
# Example Output
# Output 1:
# 2
# Output 2:
# 4

