class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # TC=O(N) SC=O(1)
        val = 0
        # logic : if len(A) is even then val is 0 else its xor of odd index element
        # here odd element present at event index like 0th is first element which is odd index
        for i in range(0, len(A) ): # [3, 4, 5]
            if i % 2 == 0:
                val = val ^ A[i ]


        if len(A) % 2 == 0:
            return 0
        else:
            return val

# Brute force : Brute force algorithms are simple and consistent, but very slow.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # TC=O(N^3) SC=O(1)
        # Try to use diff variable for each loop instead of using only i,j
        ln=len(A)
        ans=0
        for i in range(ln):
            for j in range(ln):
                if j+1>i:
                    temp=A[i:j+1]
                    for k in temp:
                        ans^=k

        # print(temp)
        return ans

# Q2. XOR-ing the Subarrays!
# Solved
# Problem Description
#
# Given an integer array A of size N.
#
# You need to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine and return this value.
#
# For example, if A = [3, 4, 5] :
#
# Subarray    Operation   Result
# 3        None            3
# 4        None            4
# 5        None            5
# 3,4      3 XOR 4         7
# 4,5      4 XOR 5         1
# 3,4,5    3 XOR 4 XOR 5   2
# Now we take the resultant values and XOR them together:
#
# 3 ⊕ 4 ⊕ 5 ⊕ 7 ⊕ 1⊕ 2 = 6 we will return 6.
#
#
#
# Problem Constraints
#
# 1 <= N <= 105
#
# 1 <= A[i] <= 108
#
#
#
# Input Format
#
# First and only argument is an integer array A.
#
#
#
# Output Format
#
# Return a single integer denoting the value as described above.
#
#
#
# Example Input
#
# Input 1:
#
#  A = [1, 2, 3]
# Input 2:
#
#  A = [4, 5, 7, 5]
#
#
# Example Output
#
# Output 1:
#
#  2
# Output 2:
#
#  0





