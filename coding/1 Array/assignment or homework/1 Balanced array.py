# this is optimal solution
# institution: Maintain PrefixSum and SuffixSum for odd and even index seperately.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # This is optimal solution with TC=O(N) and SC=O(N)
        res = 0
        ln = len(A)
        prefixEvn = [0] * ln
        prefixOdd = [0] * ln
        suffixOdd = [0] * ln
        suffixEvn = [0] * ln
        odd, even = 0, 0

        for i in range(ln):

            if i % 2 == 0:
                even += A[i]
            else:
                odd += A[i]
            prefixEvn[i] = even
            prefixOdd[i] = odd

        odd, even = 0, 0
        for i in range(ln - 1, -1, -1):

            if i % 2 == 0:
                even += A[i] # keeping previous value and adding new value as per odd and even
            else:
                odd += A[i]
            suffixEvn[i] = even
            suffixOdd[i] = odd

        # print(prefixEvn,prefixOdd,suffixEvn,suffixOdd)
        for i in range(ln):
             # suffix is viseverse becoz after deleting one number, all index will go reduce by one
             # and even and odd after thatn index alters
            if (prefixEvn[i] + suffixOdd[i]) == (prefixOdd[i] + suffixEvn[i]):
                res += 1

        return res

# BRUITE FORCE SOLUTIONS
# institution: same we delet node , do operations and insert back that node
# TC=O(N^2) ,SC=O(N^2)
# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(self, A):
#         # [1,2,3,4]
#         res=0
#         l=len(A)
#         for i in range(l):
#             val=A[i]
#             A.pop(i)
#             od=sum(A[0:l-1:2])
#             ev=sum(A[1:l-1:2])
#             if od==ev:
#                 res+=1
#             # print(od, ev, i,A)
#             A.insert(i,val)
#
#         return res



# Q3. Balance Array
# Solved
# Problem Description
#
# Given an integer array A of size N. You need to count the number of special elements in the given array.
#
# A element is special if removal of that element make the array balanced.
#
# Array will be balanced if sum of even index element equal to sum of odd index element.
#
#
#
# Problem Constraints
#
# 1 <= N <= 105
#
# 1 <= A[i] <= 109
#
#
#
# Input Format
#
# First and only argument is an integer array A of size N.
#
#
#
# Output Format
#
# Return an integer denoting the count of special elements.
#
#
#
# Example Input
#
# Input 1:
#
#  A = [2, 1, 6, 4]
# Input 2:
#
#  A = [5, 5, 2, 5, 8]
#
#
# Example Output
#
# Output 1:
#
#  1
# Output 2:
#
#  2
#
#
# Example Explanation
#
# Explanation 1:
#
#  After deleting 1 from array : {2,6,4}
#     (2+4) = (6)
#  Hence 1 is the only special element, so count is 1
# Explanation 2:
#
#  If we delete A[0] or A[1] , array will be balanced
#     (5+5) = (2+8)
#  So A[0] and A[1] are special elements, so count is 2.