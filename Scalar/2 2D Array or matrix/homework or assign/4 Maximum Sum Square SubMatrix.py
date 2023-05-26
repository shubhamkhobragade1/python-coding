class Solution:
    def solve(self, A, B):
        INF=float('-inf')
        ans=INF
        lr=len(A)
        lc=len(A[0])
        pref_sum_mat = [[0] * lc for _ in range(lr)]
        pref_sum_mat[0][0] = A[0][0]

        for i in range(1, lc):
            pref_sum_mat[0][i] = pref_sum_mat[0][i - 1] + A[0][i]

        for i in range(1, lr):
            pref_sum_mat[i][0] = pref_sum_mat[i - 1][0] + A[i][0]

        for i in range(1, lr):
            for j in range(1, lc):
                pref_sum_mat[i][j] = A[i][j] + pref_sum_mat[i][j - 1] + pref_sum_mat[i - 1][j] - pref_sum_mat[i - 1][j - 1]

        # here base on starting index we finded ending index and rest of thins r same i.e finding max sum matrix with queries
        for i in range(lr-B+1):
            for j in range(lc-B+1):
                sx = i
                sy = j
                ex =i+B-1
                ey = j+B-1
                if sx == 0 and sy == 0:
                    val = pref_sum_mat[ex][ey]
                elif sx == 0:
                    val = pref_sum_mat[ex][ey] - pref_sum_mat[ex][sy - 1]
                elif sy == 0:
                    val = pref_sum_mat[ex][ey] - pref_sum_mat[sx - 1][ey]
                else:
                    val = pref_sum_mat[ex][ey] - pref_sum_mat[sx - 1][ey] - pref_sum_mat[ex][sy - 1] + pref_sum_mat[sx - 1][sy - 1]

                ans=max(ans,val)

        return ans


# Q1. Maximum Sum Square SubMatrix
# Solved
# Hint bulb icon
# Stuck somewhere?
# Using hints is now penalty free
# Check Now
# Problem Description
# Given a 2D integer matrix A of size N x N, find a B x B submatrix where B<= N and B>= 1, such that the sum of all the elements in the submatrix is maximum.
#
#
#
# Problem Constraints
# 1 <= N <= 103.
#
# 1 <= B <= N
#
# -102 <= A[i][j] <= 102.
#
#
#
# Input Format
# First arguement is an 2D integer matrix A.
#
# Second argument is an integer B.
#
#
#
# Output Format
# Return a single integer denoting the maximum sum of submatrix of size B x B.
#
#
#
# Example Input
# Input 1:
#
#  A = [
#         [1, 1, 1, 1, 1]
#         [2, 2, 2, 2, 2]
#         [3, 8, 6, 7, 3]
#         [4, 4, 4, 4, 4]
#         [5, 5, 5, 5, 5]
#      ]
#  B = 3
# Input 2:
#
#  A = [
#         [2, 2]
#         [2, 2]
#     ]
#  B = 2
#
#
# Example Output
# Output 1:
#
#  48
# Output 2:
#
#  8
#
#
# Example Explanation
# Explanation 1:
#
#     Maximum sum 3 x 3 matrix is
#     8 6 7
#     4 4 4
#     5 5 5
#     Sum = 48
# Explanation 2:
#
#  Maximum sum 2 x 2 matrix is
#   2 2
#   2 2
#   Sum = 8