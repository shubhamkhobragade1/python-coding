# given array find the subarray of lengh k which has max sum of all value

def findMaxSubArray_bruteForce(arr, k):  # TC=O(n^2) SC=O(1)
    ln = len(arr)
    var = float('-inf')
    ans = []
    for i in range(ln - k):
        temp = sum(arr[i:k + i]) # o(N)
        if var < temp:
            var = temp
            ans = arr[i:k + i]
    return sum(ans)


def usingPrefixArray(arr, k):# tc=o(n) sc=o(1)
    ln = len(arr)
    for i in range(ln): #o(n)
        arr[i] = arr[i - 1] + arr[i]

    ans=float('-inf')
    for i in range(ln-k): #O(n-k)
        val=arr[i+k]-arr[i]
        if ans<val:
            ans=val
    return ans

def optimise(arr,k): # tc=o(n)
    ln=len(arr)
    val=sum(arr[:k]) # o(k)
    ans=float('-inf')
    for i in range(k,ln):#o(ln-k)
        val+=arr[i]-arr[i-k]
        # print(val,arr[i],arr[i-k])
        ans=max(ans,val)
    return ans


a = [-3, 4, -2, 5, 3, -2, 8, 2, -1, 4]
print(findMaxSubArray_bruteForce(a, 5))
print(usingPrefixArray(a, 5))
a = [-3, 4, -2, 5, 3, -2, 8, 2, -1, 4]
print(optimise(a, 5))
