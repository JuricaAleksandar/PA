import math
import random

def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    for i in range(1,n1):
        L[i]=A[p+id-1]
    for j in range(1,n2):
        R[j]=A[q+j]
    L[n1+1]=math.inf
    R[n2+1]=math.inf
    i=1
    j=1
    for k in range(p,r):
        if L[i]<=R[i]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
def MergeSort(A,p,r):
    if p<r:
        q=math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p,q,r)
A=[];
for i in range(100):
    a=random.randrange(100)
MergeSort(A,1,len(A))