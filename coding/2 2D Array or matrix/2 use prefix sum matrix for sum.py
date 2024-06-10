# Qn - given matrix of integer A, find the sum of given index sunmatrix
# queries=((0,1) and (1,2))
# TC=O((m*n + number_of_queries) SC=O(MN)/ sc=(1) here we an update same matrix
# previously it was multiply by quries now its addition
# in worse case we can ask sum of (0,0) to (end,end)
# and it will again going to iterate thought a matrix with number of queries times

def find_sum(l,r,mat):
    ans1=0
    lr=len(mat)
    lc=len(mat[0])
    prefix_mat=[[0]*lc for _ in range(lr)]
    prefix_mat[0][0]=mat[0][0]
    # here we can update same matrix which is SC=(1)

    for i in range(1,lc):
        prefix_mat[0][i]=prefix_mat[0][i-1]+mat[0][i]

    for i in range(1, lr):
        prefix_mat[i][0] = prefix_mat[i - 1][0] + mat[i][0]

    for i in range(1,lr):
        for j in range(1,lc):
            prefix_mat[i][j]=mat[i][j]+prefix_mat[i-1][j]+\
                             prefix_mat[i][j-1]-prefix_mat[i-1][j-1]

    print(prefix_mat)

    x1,y1=l
    x2,y2=r
    sx,sy=l
    ex,ey=r
    # ex,ey=ex+1,ey+1

    if sx==0 and sy==0:
        ans1 = prefix_mat[ex][ey]
    elif sx==0:
        # print(prefix_mat[ex][ey]  ,prefix_mat[ex][sy - 1] , prefix_mat[sx - 1][sy - 1])
        ans1 = prefix_mat[ex][ey]  - prefix_mat[ex][sy - 1] #+ prefix_mat[sx - 1][sy - 1]
    elif sy==0:
        ans1 = prefix_mat[ex][ey] - prefix_mat[sx - 1][ey] # + prefix_mat[sx - 1][sy - 1]
    else:
        # ans=    prefix_mat[x2][y2]- prefix_mat[x1-1][y2]-    prefix_mat[x2][y1-1]   + prefix_mat[x1-1][y1-1]
        ans1 = prefix_mat[ex][ey] - prefix_mat[sx - 1][ey] - prefix_mat[ex][sy - 1] + prefix_mat[sx - 1][sy - 1]

    return ans1

# queries=[(0,1),(1,3)]
queries=[(1,2),(3,4)]
a=[
    [1,3,5,2,-1],
    [4,8,5,0,6],
    [10,20,1,3,5],
    [1,5,-5,10,6]
]
# a=[[1,2,3],[4,5,6],[7,8,9]]

val=find_sum(queries[0],queries[1],a)
print(val)


