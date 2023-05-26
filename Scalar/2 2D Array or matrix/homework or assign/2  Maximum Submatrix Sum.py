class Solution:
    # @param A : list of list of integers
    # @return an long
    def solve(self, mat):
        lc = len(mat[0])
        lr = len(mat)
        suff_sum_mat = [[0] * lc for _ in range(lr)]
        suff_sum_mat[lr - 1][lc - 1] = mat[lr - 1][lc - 1]
        ans = mat[lr - 1][lc - 1]
        for i in range(lr - 2, -1, -1):
            suff_sum_mat[i][lc - 1] = suff_sum_mat[i + 1][lc - 1] + mat[i][lc - 1]
            ans = max(ans, suff_sum_mat[i][lc - 1])  # here some submatrix is form that also need to check

        for i in range(lc - 2, -1, -1):
            suff_sum_mat[lr - 1][i] = suff_sum_mat[lr - 1][i + 1] + mat[lr - 1][i]
            ans = max(ans, suff_sum_mat[lr - 1][i])

        for i in range(lr - 2, -1, -1):
            for j in range(lc - 2, -1, -1):
                suff_sum_mat[i][j] = mat[i][j] + suff_sum_mat[i + 1][j] + suff_sum_mat[i][j + 1] - suff_sum_mat[i + 1][
                    j + 1]
                ans = max(ans, suff_sum_mat[i][j])
        # print(suff_sum_mat)

        return ans
# Q3. Maximum Submatrix Sum
# Solved
# Hint bulb icon
# Stuck somewhere?
# Using hints is now penalty free
# Check Now
# Problem Description
# Given a row-wise and column-wise sorted matrix A of size N * M.
# Return the maximum non-empty submatrix sum of this matrix.
#
#
# Problem Constraints
# 1 <= N, M <= 1000
# -109 <= A[i][j] <= 109
#
#
# Input Format
# The first argument is a 2D integer array A.
#
#
# Output Format
# Return a single integer that is the maximum non-empty submatrix sum of this matrix.
#
#
# Example Input
# Input 1:-
#     -5 -4 -3
# A = -1  2  3
#      2  2  4
# Input 2:-
#     1 2 3
# A = 4 5 6
#     7 8 9
#
#
# Example Output
# Output 1:-
# 12
# Output 2:-
# 45
#
#
# Example Explanation
# Expanation 1:-
# The submatrix with max sum is
# -1 2 3
#  2 2 4
#  Sum is 12.
# Explanation 2:-
# The largest submatrix with max sum is
# 1 2 3
# 4 5 6
# 7 8 9
# The sum is 45.