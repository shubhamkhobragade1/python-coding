# Given intefer array, return the final array after performing the
# multiple queries(start,end,val) to all numbers from index i to n-1
# here in queries we received end as well
def addQuries(qr,arr):
    # TC=queries*ln
    ln=len(arr)
    for s,e,val in qr:
        for k in range(s,e+1):
            arr[k]+=val
    return arr

# this is optimised using pefix array
def usePrefArray(qr,arr):# here TC=quries + ln
# institution is that in we need to add val up to end given but in prefix array val will get added up to end of array
# so by placing same element negative val at end+1 make its null effect
    for s,e,val in qr:
        arr[s]+=val
        arr[e+1]-=val

    ln=len(arr)
    for i in range(1,ln):
        arr[i]=arr[i-1]+arr[i]
    return arr


queries=[(1,3,2),(2,5,3),(5,6,-1)]
A=[0]*10
print(addQuries(queries,A))

queries=[(1,3,2),(2,5,3),(5,6,-1)]
A=[0]*10
print(usePrefArray(queries,A))