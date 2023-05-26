
class Solution:
    # TC=O(N) sc=(1)
    # idea is reverse list- add one to last element-chech if first ele is 10 then append 0 and make last ele as 1
    def plusOne(self, A):
        ln = len(A)
        # A=[]
        if ln == 0:
            return A
        elif ln==1:
            A[0 ]+=1
            return list(str(A[0]))

        while (A[0] == 0 ):
            A.remove(0)
            if len(A )==0:
                break

        ln = len(A)
        for i in range(ln // 2):
            A[i], A[-i - 1] = A[-i - 1], A[i]

        carry = 0
        A[0] += 1

        for i in range(ln):

            val =A[i] + carry
            rem = val % 10
            carry = val // 10
            # print(A,val,rem,carry)
            if carry != 0:
                A[i] = rem
            else: # in eg=[1,9,9] this needed to add one at first which done in val here
                A[i] = val

        # print(A,carry)
        if A[ln - 1] == 10:
            A.append(0)
            A[ln] = 1
        if carry == 1:
            A.append(0)
            A[-1] += 1

        ln = len(A)

        for i in range(ln // 2):
            A[i], A[-i - 1] = A[-i - 1], A[i]

        return A

# Q1. Add One To Number
# Solved
# character backgroundcharacter
# Stuck somewhere?
# Ask for help from a TA and get it resolved.
# Get help from TA.
# Problem Description
# Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
#
# The digits are stored such that the most significant digit is at the head of the list.
#
# NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :
#
# Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
# A: For the purpose of this question, YES
# Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
# A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
#
#
# Problem Constraints
# 1 <= size of the array <= 1000000
#
#
#
# Input Format
# First argument is an array of digits.
#
#
#
# Output Format
# Return the array of digits after adding one.
#
#
#
# Example Input
# Input 1:
#
# [1, 2, 3]
#
#
# Example Output
# Output 1:
#
# [1, 2, 4]
#
#
# Example Explanation
# Explanation 1:
#
# Given vector is [1, 2, 3].
# The returned vector should be [1, 2, 4] as 123 + 1 = 124.