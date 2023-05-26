class Solution:

    def solve(self, A):
        mat = [[0 for i in range(A)]for j in range(A)]
        val=1
        i,j=0,0
        direct='Right'
        while(val<=A**2):
            mat[i][j]=val
            # print(mat, val, (i, j))
            val+=1
            if direct=='Right':
                j+=1
                if j==A or mat[i][j]!=0:
                    direct='Down'
                    j-=1
                    i+=1
            elif direct=='Down':
                i+=1
                if i==A or mat[i][j]!=0:
                    direct='Left'
                    i-=1
                    j-=1
            elif direct=='Left':
                j-=1
                if j<0:
                    j=0
                    i-=1
                    direct='Up'
                elif mat[i][j]!=0:
                    j+=1
                    i-=1
                    direct='Up'
            elif direct=='Up':
                i-=1
                if i>=0:
                    if mat[i][j]!=0:
                        j+=1
                        i+=1
                        direct='Right'
                else:
                    i+=1
        for i in mat:
            print(i)
        return mat



a= 5
print(Solution().solve(a))
# Q3. Spiral Order Matrix II
# Solved
# Problem Description
# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.
#
#
#
# Problem Constraints
# 1 <= A <= 1000
#
#
#
# Input Format
# First and only argument is integer A
#
#
# Output Format
# Return a 2-D matrix which consists of the elements added in spiral order.
#
#
#
# Example Input
# Input 1:
#
# 1
# Input 2:
#
# 2
# Input 3:
#
# 5
#
#
# Example Output
# Output 1:
#
# [ [1] ]
# Output 2:
#
# [ [1, 2], [4, 3] ]
# Output 2:
#
# [ [1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9] ]