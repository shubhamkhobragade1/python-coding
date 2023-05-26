class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        ln = len(A)
        if int('1' + '0' * ln) - int(A) == 1:  # if number is like '999' series
            return str(int(A) + 2)

        else:
            if ln % 2 == 0:
                left = A[:ln // 2]
                val = left + left[::-1]
                if int(val) <= int(A):
                    left = str(int(left) + 1)
                    val = left + left[::-1]
                return val
            else:
                left = A[:ln // 2]
                val = left + A[ln // 2] + left[ln // 2 + 1::-1]
                if int(val) <= int(A):  # if newly formed number less than given
                    left = str(int(left) + 1)
                    val = left + A[ln // 2] + left[ln // 2 + 1::-1]
                return val

# Q5. Next Smallest Palindrome!
# Attempted
# Problem Description
#
# Given a numeric string A representing a large number you need to find the next smallest palindrome greater than this number.
#
#
#
# Problem Constraints
#
# 1 <= |A| <= 100
#
# A doesn't start with zeroes and always contain digits from 0-9.
#
#
#
# Input Format
#
# First and only argument is an string A.
#
#
#
# Output Format
#
# Return a numeric string denoting the next smallest palindrome greater than A.
#
#
#
# Example Input
#
# Input 1:
#
#  A = "23545"
# Input 2:
#
#  A = "999"
#
#
# Example Output
#
# Output 1:
#
#  "23632"
# Output 2:
#
#  "1001"