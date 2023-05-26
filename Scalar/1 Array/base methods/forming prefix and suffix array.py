class Solution:
    # TC=O(N) SC=O(N)
    def solve(self, A):
        ln=len(A)
        suff=[1]*ln
        suff[ln-1]=A[ln-1]
        pref=[1]*ln
        pref[0]=A[0]
        for i in range(1,ln): # this is fix conditions for suff array
            pref[i]=pref[i-1]*A[i]

        for i in range(ln-2,-1,-1): # this is fix conditions for suff array
            suff[i]=suff[i+1]*A[i]
