# this algorithm has 3 cases
# TC=O(N) And SC=O(1)
def findMaxSubArray(arr):
    # case 1: if all element in array is not negative(0->n)
    # here ans is sum of all
    ans=sum(arr)
    # case 2 : if all non positive n<0
    ans1=min(arr)
    # for combinition of all
    # here idea is we r keep on adding but at any instant if sum becom less than 0 then we assing it as 0
    sm=0
    ans2=0
    for i in arr:
        sm+=i
        if sm<0:
            sm=0
        ans2=max(ans2,sm)

    return max(ans,ans1,ans2)