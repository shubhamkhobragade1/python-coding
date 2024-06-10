class Solution1:
    # this is selection sort which is brute force
    def solve(self, A):
        ans=0
        ln=len(A)
        # this will be brute force and tc=o(N**2) which is selections sort
        for i in range(ln):
            min_ind=i
            for j in range(i+1,ln):
                if A[min_ind]>A[j]:
                    min_ind=j
            if min_ind!=i:
                A[min_ind],A[i]=A[i],A[min_ind]
                ans+=1
        # print(A)
        return ans

class Solution:
    def solve(self, A, B):
        INF = float('inf')
        ans = INF

        ln = 0
        for i in A:  # here i have finded how many element is less than B
            if i <= B:
                ln += 1

        # now we will find window where max of element less than B is present
        # and in that window element greater than B there is the answer
        count_of_max_element_in_window = 0
        for i in A[:ln]:
            if i > B:
                count_of_max_element_in_window += 1

        for i in range(ln, len(A)):
            if A[i] > B:
                count_of_max_element_in_window += 1
            if A[i - ln] > B:
                count_of_max_element_in_window -= 1

            ans = min(ans, count_of_max_element_in_window)

        return ans if ans != INF else 0

# Q2. Minimum Swaps
# Solved
# Hint bulb icon
# Stuck somewhere?
# Using hints is now penalty free
# Check Now
# Problem Description
#
# Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.
#
# Note: It is possible to swap any two elements, not necessarily consecutive.
#
#
#
# Problem Constraints
#
# 1 <= length of the array <= 100000
# -109 <= A[i], B <= 109
#
#
#
# Input Format
#
# The first argument given is the integer array A.
# The second argument given is the integer B.
#
#
#
# Output Format
#
# Return the minimum number of swaps.
#
#
#
# Example Input
#
# Input 1:
#
#  A = [1, 12, 10, 3, 14, 10, 5]
#  B = 8
# Input 2:
#
#  A = [5, 17, 100, 11]
#  B = 20
#
#
# Example Output
#
# Output 1:
#
#  2
# Output 2:
#
#  1
#
#
# Example Explanation
#
# Explanation 1:
#
#  A = [1, 12, 10, 3, 14, 10, 5]
#  After swapping  12 and 3, A => [1, 3, 10, 12, 14, 10, 5].
#  After swapping  the first occurence of 10 and 5, A => [1, 3, 5, 12, 14, 10, 10].
#  Now, all elements less than or equal to 8 are together.
# Explanation 2:
#
#  A = [5, 17, 100, 11]
#  After swapping 100 and 11, A => [5, 17, 11, 100].
#  Now, all elements less than or equal to 20 are together.
#