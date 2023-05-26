# this will help full when doing sum in array
# Qn find subarray which has max sum
def withoutCarrayF(arr):# TC=O(N^3)
    ans=float('-inf')
    ln=len(arr)
    subArrays=[]
    for i in range(ln):# TC=O(N)
        h=[]
        for j in range(i,ln):# TC=O(N)
            h.append(arr[j])
            temp=h[:]# once we append whole array so TC=O(N)
            subArrays.append(temp) # once we append whole array so TC=O(N)
    print(subArrays)
    for i in subArrays:
        s=sum(i)
        if s>ans:
            ans=s
    return ans

def carryForward(arr): # TC=O(N^2)
    ln = len(arr)
    ans=float('-inf')
    for i in range(0,ln): # 1->5
        carry=0
        for j in range(i,ln):
            carry+=arr[j]
            ans=max(ans,carry)
    return ans

a=[1,2,3,4,-5,-6]
print(withoutCarrayF(a))
print(carryForward(a))


