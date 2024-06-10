# find the sum of all subarray
def findSum(arr): # tc=o(n^2)
    s=0
    ln=len(arr)
    for i in range(ln):
        temp=0
        for j in range(i,ln):
            temp+=arr[j]
            s+=temp
    return s
# 8+[8,6]+[8,6,5]+6+[6,5]+5=8*3+6*4+5*3=63


# here we dan find element repeating specific numbers of time
# eg for 5 in arr=[8,6,5,7,10,5],we can see that 5 will e part of subarray when
# start indx=[0,1,2] and end indx=[2,3,4,5] which=5*(2+1)*(6-2)=60
# so sum of all subarray= arr[i]*(i+1)*(n-i)

def optimise(arr):
    s=0
    ln=len(arr)
    for i in range(ln):
        s+=arr[i]*(i+1)*(ln-i)
    return s

a=[8,6,5]
b=[8,6,5,7,10,5]
print(findSum(a))
print(optimise(a))
print(optimise(b))

# C:\Temp\python.exe "C:\Users\Shubham  Khobragade\PycharmProjects\pythonProject4\Scalar\1 Array\base problem of class\4 sum of sums of all subarrays.py"
# 63
# 63
# 382