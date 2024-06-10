# given integer array,find equillibrium index of array
# equillibrium index where sum of element on left and right is same

def findIndex(arr):
    for i in range(1,len(arr)):
        arr[i]=arr[i-1]+arr[i]
    ans=[]
    ln=len(arr)
    # print(arr)
    for i in range(1,ln):
        if arr[i-1]==(arr[ln-1]-arr[i]):
            ans.append(i)

    return ans

a=[-7,1,5,2,-4,3,0]
print(findIndex(a))