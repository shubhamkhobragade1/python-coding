# this sliding windwo we can use for same size subarray for like find max sum,
# add new and remove previous first
def slide(Wsize,arr):
    temp=ans=sum(arr[:Wsize])
    for i in range(Wsize,len(arr)):
        temp+=arr[i]-arr[i-Wsize]
        ans=max(ans,)
