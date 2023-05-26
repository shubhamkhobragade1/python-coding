# Given intefer array, return the final array after performing the
# multiple queries(i,x) to all numbers from index i to n-1
def addQuries(qr,arr):
    # TC=queries*ln
    ln=len(arr)
    for i,j in qr:
        for k in range(i,ln):
            arr[k]+=j
    return arr

# this is optimised using pefix array
def usePrefArray(qr,arr):# here TC=quries + ln

    for i,j in qr:
        arr[i]+=j

    ln=len(arr)
    for i in range(1,ln):
        arr[i]=arr[i-1]+arr[i]
    return arr

queries=[(1,3),(4,2),(3,1)]
A=[0]*6
print(addQuries(queries,A))

queries=[(1,3),(4,2),(3,1)]
A=[0]*6
print(usePrefArray(queries,A))