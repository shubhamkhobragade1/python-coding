# Qn - u r given row and column wise sorted matrx. return the max subarray matrxi
# TC=o(MN) SC=O(NM) /O(1) if updated same array
def find_sum(mat):
    ans=0
    lc=len(mat[0])
    lr=len(mat)
    suff_sum_mat=[[0]*lc for _ in range(lr)]
    # if col and row sorted in ascending order then use suffix sum matrx
    # if in descending order then use prefix sum matris
    # bcoz we r taking max element as reference which is at end in ascending order
    suff_sum_mat[lr-1][lc-1]=mat[lr-1][lc-1]
    for i in range(lr - 2, -1, -1):
        suff_sum_mat[i][lc-1]=suff_sum_mat[i+1][lc-1]+mat[i][lc-1]

    for i in range(lc - 2, -1, -1):
        suff_sum_mat[lr-1][i]=suff_sum_mat[lr-1][i+1]+mat[lr-1][i]

    ans=mat[lr-1][lc-1]
    for i in range(lr-2,-1,-1):
        for j in range(lc-2,-1,-1):
            suff_sum_mat[i][j]=mat[i][j]+suff_sum_mat[i+1][j] +suff_sum_mat[i][j+1]- suff_sum_mat[i+1][j+1]
            ans=max(ans,suff_sum_mat[i][j])


    return ans

a=[
    [-5,-2,1,3],
    [-4,0,3,4],
    [-2,1,6,8]
]

val=find_sum(a)
print(val)


