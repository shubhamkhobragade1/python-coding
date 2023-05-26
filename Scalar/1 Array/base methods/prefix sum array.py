# this subarray going to have sum of element upto that index(all prefix element)
# precomputation: store some precalculation so that answering query can be optimise
def prefixArray(arr): # [1,2,3,4,5,6]
    ln = len(arr)  # 6
    prefix=[0]*ln # SC=O(N) [1]
    prefix[0]= arr[0]  # SC=O(N) [1]

    for i in range(1,ln): # 1->5
        prefix[i]=prefix[i-1]+arr[i]
    return prefix

def prefixArray_inPlace(arr):  # SC=O(1)
    ln=len(arr)
    for i in range(1,ln):
        arr[i]=arr[i-1]+arr[i]
    return arr

a=[1,2,3,4,5,6]
print(prefixArray(a))
print(prefixArray_inPlace(a))
