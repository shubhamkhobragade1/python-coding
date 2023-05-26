class Solution:# brute force : TC=N^2
    # Constraint 1 to 10^5-so if TC is =N^2 then for last value time is =(10^5)^2=10^10
    # -generaly time allowed is one second=10^8
    # So for max value as per constrain is (10^5)* (time complexity). So this needs to be less than 10^8
    # For TC=N^2 it is (10^5)^2=10^10 which will exceed TC
    def cntBits(self, A):

        # find all pairs
        pairs = []
        ln = len(A)
        ans = 0
        for i in range(ln):
            for j in range(i, ln):
                # pairs.append([A[i],A[j]])

                val = bin(A[i] ^ A[j])[2:]
                ans += val.count('1')

        # find xor and count diff count bits

        # for i,j in pairs:
        #     val=bin(i^j)[2:]
        #     ans+=val.count('1')

        return ans * 2


class Solution1: # TC=32*N where for max contrain TC=32*n*(10^5)=~ 10*6
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        ans = 0
        mod = 1000000007
        # Fits in a 32-bit integer: In many programming languages, the maximum value of a 32-bit signed integer
        # is 2^31 - 1, which is approximately 2.1 billion. Since 1000000007 is smaller than this limit,
        # it can be stored within a 32-bit integer without overflowing.
        #
        # Avoids overflow: When performing arithmetic operations on large numbers, such as multiplication or
        # exponentiation, the intermediate results can quickly become very large. By taking the modulo
        # 1000000007 at each step, the values are kept within a manageable range, reducing the chance of
        # overflow errors.
        for i in range(32):  # 32 is base on constrain given in problem
            c0, c1 = 0, 0 # conting 0 and 1 bits
            for val in A:
                if val & (1 << i): # conting and summing up i'th bit of each element
                    c1 += 1
                else:
                    c0 += 1

            ans += 2 * (c0 * c1) # 2 is bcoz there will be 2 pair for same bit like (i,j) and (j,i)
        ans %= mod
        return ans
# Q8. Different Bits Sum Pairwise
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# We define f(X, Y) as the number of different corresponding bits in the binary representation of X and Y.
# For example, f(2, 7) = 2, since the binary representation of 2 and 7 are 010 and 111, respectively. The first and the third bit differ, so f(2, 7) = 2.
#
# You are given an array of N positive integers, A1, A2,..., AN. Find sum of f(Ai, Aj) for all pairs (i, j) such that 1 ≤ i, j ≤ N. Return the answer modulo 109+7.
#
#
#
# Problem Constraints
# 1 <= N <= 10^5
#
# 1 <= A[i] <= 2^31 - 1
#
# Input Format
# The first and only argument of input contains a single integer array A.
#
# Output Format
# Return a single integer denoting the sum.
#
# Example Input
# Input 1:
#
#  A = [1, 3, 5]
# Input 2:
#
#  A = [2, 3]
#
#
# Example Output
# Ouptut 1:
#
#  8
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5)
#  = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8
# Explanation 2:
#
#  f(2, 2) + f(2, 3) + f(3, 2) + f(3, 3) = 0 + 1 + 1 + 0 = 2