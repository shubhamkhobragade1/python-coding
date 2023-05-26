# https://www.scaler.com/academy/mentee-dashboard/class/7327/assignment/problems/11949/?navref=cl_pb_nv_tb
class Solution:# TC=O(N^4)  Brute force
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        r = len(A)
        c = len(A[0])

        def check(a, b): #TC=O(N^2)
            que = [(a, b)]
            # print((a, b), "-----------------------------------------")
            fl2, fl1 = False, False
            vis = []
            while (que):
                i, j = que.pop(0)
                if (i == 0 and 0 <= j < c) or (j == 0 and 0 <= i < r):
                    fl1 = True
                    # print((i,j),'blue')
                if ((j==c-1 and 0<=i<r )or (i==r-1 and 0<=j<c)):
                    fl2 = True
                    # print((i,j),'red')
                for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < r and 0 <= y < c and (x, y) not in vis:
                        if A[x][y] <= A[i][j]:
                            vis.append((x, y))
                            que.append((x, y))
            # print(fl1 and fl2,f'blue={fl1}',f'red={fl2}')
            # print(vis)
            return fl1 and fl2

        res = 0
        for i in range(r): # TC=O(N^2)
            for j in range(c):
                if check(i, j):# TC=O(N^2)
                    # print((i,j),end=' ')
                    res += 1

        return res

# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def is_valid(self,x,y,row,col):
#         if x>=0 and y>=0 and x<row and y <col:
#             return True
#         return False
#
#     def solve(self, A):
#          # istitution:
#          # # TC=O(N^2)
#         # here we will make all corners as 1 for both the side separatly if blue/atlantic and red/pacific
#         # we r making value at index in matrix as 1 if we found increasing in any direction
#         # which is opposite to as water flow from up to down
#         row=len(A)
#         col=len(A[0])
#         blue=[[0 for _ in range(col)]for _ in range(row)] # TC=O(N^2)
#         red=[[0 for _ in range(col)]for _ in range(row)]
#         stack=[]
#         for i in range(col):
#             blue[0][i]=1
#             stack.append((0,i))
#
#         for i in range(1,row):
#             blue[i][0]=1
#             stack.append((i,0))
#
#
#
#         # print(red,'\n',blue)
#         while(stack):# TC=O(N^2)
#             a,b=stack.pop()
#             for x,y in [(a,b-1),(a-1,b),(a+1,b),(a,b+1)]:
#                 if self.is_valid(x,y,row,col):
#                     if blue[x][y]==0 and A[x][y]>=A[a][b] :
#                         stack.append((x,y))
#                         blue[x][y]+=1
#
#         res=0
#
#         for i in range(col-1,-1,-1):# TC=O(N)
#             red[row-1][i]=1
#             stack.append((row-1,i))
#
#         for i in range(row-2,-1,-1):
#             red[i][col-1]=1
#             stack.append((i,col-1))
#
#
#         while(stack):# TC=O(N^2)
#             a,b=stack.pop()
#             if blue[a][b]==1 and red[a][b]==1:
#                 res+=1
#
#             for x,y in [(a,b-1),(a-1,b),(a+1,b),(a,b+1)]:
#                 if self.is_valid(x,y,row,col):
#                     if red[x][y]==0 and A[x][y]>=A[a][b] :
#                         stack.append((x,y))
#                         red[x][y]=1
#         # print(red,'\n',blue)
#         return res


# Q1. Water Flow
# Attempted
# Problem Description
#
# Given an N x M matrix A of non-negative integers representing the height of each unit cell in a continent, the "Blue lake" touches the left and top edges of the matrix and the "Red lake" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
#
# Find the number of cells from where water can flow to both the Blue and Red lake.
#
#
#
# Problem Constraints
#
# 1 <= M, N <= 1000
#
# 1 <= A[i][j] <= 109
#
#
#
# Input Format
#
# First and only argument is a 00 2D matrix A.
#
#
#
# Output Format
#
# Return an integer denoting the number of cells from where water can flow to both the Blue and Red lake
#
#
#
# Example Input
#
# Input 1:
#
#  A = [
#        [1, 2, 2, 3, 5]
#        [3, 2, 3, 4, 4]
#        [2, 4, 5, 3, 1]
#        [6, 7, 1, 4, 5]
#        [5, 1, 1, 2, 4]
#      ]
# Input 2:
#
#  A = [
#        [2, 2]
#        [2, 2]
#      ]
#
#
# Example Output
#
# Output 1:
#
#  7
# Output 2:
#
#  4
#
#
# Example Explanation
#
# Explanation 1:
#
#  Blue Lake ~   ~   ~   ~   ~
#         ~  1   2   2   3  (5) *
#         ~  3   2   3  (4) (4) *
#         ~  2   4  (5)  3   1  *
#         ~ (6) (7)  1   4   5  *
#         ~ (5)  1   1   2   4  *
#            *   *   *   *   * Red Lake
#  Water can flow to both lakes from the cells denoted in parentheses.