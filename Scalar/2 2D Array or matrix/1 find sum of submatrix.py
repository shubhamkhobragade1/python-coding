# Qn - given matrix of integer A, find the sum of given index sunmatrix
# queries=((0,1) and (1,2))
# TC=O((m*n*number_of_queries) in worse case we can ask sum of (0,0) to (end,end)
# and it will again going to iterate thought a matrix with number of queries times

def find_sum(l,r,mat):
    ans=0
    x1,y1=l
    x2,y2=r
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            ans+=mat[i][j]

    return ans


queries=[(1,2),(3,4)]

a=[
    [1,3,5,2,-1],
    [4,8,5,0,6],
    [10,20,1,3,5],
    [1,5,-5,10,6]
]

val=find_sum(queries[0],queries[1],a)
print(val)


