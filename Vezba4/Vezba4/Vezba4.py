import random
import time
import math

def BucketSort(A):
    B=[]
    n=len(A)
    for i in range(0,n):
        B.append(0)
    for i in range(0,n):
        B[math.floor(n*A[i])]=A[i]
    for j in range(1,len(B)):
        key=B[j]
        i=j-1
        while i>=0 and B[i]>key:
            B[i+1]=B[i]
            i=i-1
        B[i+1]=key

def Partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r,1):
        if A[j]<=x:
            i=i+1
            pom=A[i]
            A[i]=A[j]
            A[j]=pom
    pom=A[i+1]
    A[i+1]=A[r]
    A[r]=pom
    return i+1

def RandomizedPartition(A,p,r):
    i=random.randint(p,r)
    return Partition(A,p,r)

def RandomizedQuicksort(A,p,r):
    if p<r:
        q = RandomizedPartition(A,p,r)
        RandomizedQuicksort(A,p,q-1)
        RandomizedQuicksort(A,q+1,r)

Q=[]
B=[]
for i in range(1,101):
    B.append(random.randint(1,101))
    Q.append(random.randint(1,101))
print("Pre-bucketsort")
print(B)
BucketSort(B)
print("Bucketsorted")
print(B)
print("Pre-quicksort")
print(Q)
RandomizedQuicksort(Q,0,len(Q)-1)
print("Quicksorted")
print(Q)
