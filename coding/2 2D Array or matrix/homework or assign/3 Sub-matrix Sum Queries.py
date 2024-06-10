class Solution:
    def solve(self, A, B, C, D, E):
        lr = len(A)
        lc = len(A[0])
        pref_sum_mat = [[0] * lc for _ in range(lr)]
        pref_sum_mat[0][0] = A[0][0]

        for i in range(1, lc):
            pref_sum_mat[0][i] = pref_sum_mat[0][i - 1] + A[0][i]

        for i in range(1, lr):
            pref_sum_mat[i][0] = pref_sum_mat[i - 1][0] + A[i][0]

        for i in range(1, lr):
            for j in range(1, lc):
                pref_sum_mat[i][j] = A[i][j] + pref_sum_mat[i][j - 1] + pref_sum_mat[i - 1][j] - pref_sum_mat[i - 1][
                    j - 1]

        # print(pref_sum_mat,'hi')
        # 2*(10**9)
        ans = []
        for i in range(len(B)):
            sx = B[i] - 1
            sy = C[i] - 1
            ex = D[i] - 1
            ey = E[i] - 1
            if sx == 0 and sy == 0:
                val = pref_sum_mat[ex][ey]
            elif sx == 0:
                val = pref_sum_mat[ex][ey] - pref_sum_mat[ex][sy - 1]
            elif sy == 0:
                val = pref_sum_mat[ex][ey] - pref_sum_mat[sx - 1][ey]
            else:
                val = pref_sum_mat[ex][ey] - pref_sum_mat[sx - 1][ey] - pref_sum_mat[ex][sy - 1] + pref_sum_mat[sx - 1][
                    sy - 1]

            val = val % (10 ** 9 + 7)
            ans.append(val)

        return ans

# Q2. Sub-matrix Sum Queries
# Solved
# Hint bulb icon
# Stuck somewhere?
# Using hints is now penalty free
# Check Now
# Problem Description
# Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.
#
# Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.
#
# NOTE:
#
# Rows are numbered from top to bottom, and columns are numbered from left to right.
# The sum may be large, so return the answer mod 109 + 7.
# Also, select the data type carefully, if you want to store the addition of some elements.
# Indexing given in B, C, D, and E arrays is 1-based.
# Top Left 0-based index = (B[i] - 1, C[i] - 1)
# Bottom Right 0-based index = (D[i] - 1, E[i] - 1)
#
#
# Problem Constraints
# 1 <= N, M <= 1000
# -100000 <= A[i] <= 100000
# 1 <= Q <= 100000
# 1 <= B[i] <= D[i] <= N
# 1 <= C[i] <= E[i] <= M
#
#
#
# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer array B.
# The third argument given is the integer array C.
# The fourth argument given is the integer array D.
# The fifth argument given is the integer array E.
# (B[i], C[i]) represents the top left corner of the i'th query.
# (D[i], E[i]) represents the bottom right corner of the i'th query.
#
#
#
# Output Format
# Return an integer array containing the submatrix sum for each query.
#
#
#
# Example Input
# Input 1:
#
#  A = [   [1, 2, 3]
#          [4, 5, 6]
#          [7, 8, 9]   ]
#  B = [1, 2]
#  C = [1, 2]
#  D = [2, 3]
#  E = [2, 3]
# Input 2:
#
#  A = [   [5, 17, 100, 11]
#          [0, 0,  2,   8]    ]
#  B = [1, 1]
#  C = [1, 4]
#  D = [2, 2]
#  E = [2, 4]
#
#
# Example Output
# Output 1:
#
#  [12, 28]
# Output 2:
#
#  [22, 19]
#
#
# Example Explanation
# Explanation 1:
#
#  For query 1: Submatrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
#  For query 2: Submatrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
# Explanation 2:
#
#  For query 1: Submatrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
#  For query 2: Submatrix contains elements: 11 and 8. So, their sum is 19