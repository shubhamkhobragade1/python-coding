# Qn - find sum of all submatrix
# here to form all or sub matrix TC is [n(n+1)/2]* [m(m+1)/2]
# so if we solve TC=(mn)^2 then we can find sum
# so we can use here method of contibution means how many times pariculat element is repeating
# we can see for particular element(i,j) contribution is=all submatrix end with that point + all submatrix start with this
# = topleft((i+1) * (j+1))* rightbotom((n-i) * (m-j ))
# sum of (i to j) = A[i][j]*(i+1)*(j+1)*(n-i)*(m-j)
# TC=O(MN)


def find_sum(mat):
    ans=0
    lr = len(mat)
    lc = len(mat[0])

    for i in range(lr):
        for j in range(lc):
            ans+=mat[i][j] * (i + 1) * (j + 1) * (lr - i) * (lc - j)

    return ans

a1=[
    [1,3,5,2,-1],
    [4,8,5,0,6],
    [10,20,1,3,5],
    [1,5,-5,10,6]
]
a=[[1,12,3],[3,2,1]]  # 160
val=find_sum(a)
print(val)





