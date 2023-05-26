# Given N buildings,with height of each building . find the rain
# water trapped in between buildings

# here we r moving from curr index in right and left direction to find max height
# TC=O(N^2) # SC=O(1)
def findWaterTrapped(arr):
    ans=0
    ln=len(arr)
    for j in range(1,ln-1):# TC=O(N)
        i=j
        l=i-1
        r=i+1
        lm=rm=0
        if i-1>=0:lm=arr[l]
        if i+1<ln:rm=arr[r]
        while(i-1>=0 ):# TC=O(N)
            i-=1
            if arr[i]>lm:
                lm=arr[i]

        while(i+1<ln):# TC=O(N)
            i+=1
            if arr[i]>rm:
                rm=arr[i]

        val=min(rm,lm)
        if val > arr[j]:
            ans+=abs(min(rm,lm)-arr[j])
        # print(ans,val,arr[j],j,'nn',lm,rm)

    return ans

# here institution is that we create 2 array which keep track of max min for particular index
# and can access direactly
# # TC=O(N) SC=O(N)
def usingPrefixTypeArr(arr):
    ln=len(arr)
    lmx=[0]*ln
    rmx=[0]*ln
    lmx[0]=arr[0]
    rmx[-1]=arr[-1]
    for i in range(1,ln):
        if arr[i]>lmx[i-1]:
            lmx[i]=arr[i]
        else:
            lmx[i]=lmx[i-1]

    for i in range(ln-2,-1,-1):
        if arr[i]>rmx[i+1]:
            rmx[i]=arr[i]
        else:
            rmx[i]=rmx[i+1]

    ans=0
    # print(lmx,rmx)
    for i in range(1,ln-1):

        val=min(lmx[i-1],rmx[i+1])
        if val>arr[i]:
            ans+=abs(val-arr[i])
        # print(val, i,ans)

    return ans

def optimiseSolution(arr):
    ln=len(arr)
    l=0
    # print('hi')
    r=ln-1
    ans=0
    while(l<r):
        while(l<r and arr[l]<=arr[l+1]):
            l+=1
        while(l<r and arr[r-1]>=arr[r]):
            r-=1

        while(l<r):
            left=arr[l]
            right=arr[r]
            if left<=right:
                while(l<r and left>=arr[l]):
                    ans+=left-arr[l]
                    # left=arr[l+1]
                    l+=1
            else:
                while(l<r and right>=arr[r]):
                    ans+=right-arr[r]
                    # right=arr[r]
                    r -= 1
    # print('hi')
    return ans

Array=[6,3,2,4,1,3,5,3,4]
# print(findWaterTrapped(Array))
# print(usingPrefixTypeArr(Array))
print(optimiseSolution(Array))
