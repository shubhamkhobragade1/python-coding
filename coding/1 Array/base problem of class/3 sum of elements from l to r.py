# given intefer array of size n and q queries in the form of l to r
# find the sum of elements from l to r

def findSum(arr,l,r):
    ln=len(arr)
    for i in range(1,ln):
        arr[i]=arr[i-1]+arr[i]

    return arr[r]-arr[l] # sum upto r -sum upto l

a=[1,2,3,4,5,6]
print(findSum(a,2,4))
