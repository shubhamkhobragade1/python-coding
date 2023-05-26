# find the subarray with max sum of all subarray

# TC=O(N^2) SC=O(1)
def findMaxSubArray(arr):
    ans=arr[0]
    ln=len(arr)
    for i in range(ln):
        h=0
        for j in range(i,ln):
            h+=arr[j]
            ans=max(h,ans)

    return ans

# this algorithm has 3 cases
# TC=O(N) And SC=O(1)
def findMaxSubArray1(arr):
    # case 1: if all element in array is not negative(0->n)
    # here ans is sum of all
    ans=sum(arr)
    # case 2 : if all non positive n<0
    ans1=min(arr)
    # for combinition of all
    # here idea is we r keep on adding but at any instant if sum becom less than 0 then we assing it as 0
    ans2 = 0
    sm = 0
    for i in arr:
        sm += i
        if sm < 0:
            sm = 0
        ans2 = max(ans2, sm)

    return ans2 if ans2 != 0 else max(arr)
a=[10,-5,7,8,-1,2]
print(findMaxSubArray(a))
print(findMaxSubArray1(a))


