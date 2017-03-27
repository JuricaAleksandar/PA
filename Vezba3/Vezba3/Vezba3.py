import math
import time
import random

L=[]
for i in range (7):    
    L.append(random.randrange(1,101,1))
hs=len(L)

def MaxHeapify(A,i,hs):
    largest=0
    l=2*i
    r=2*i+1
    if l<=hs and A[l]>A[i]:
        largest=l
    else:
        largest=i
    if r<=hs and A[r]>A[largest]:
        largest=r
    if largest!=i:
        pom=A[i]
        A[i]=A[largest]
        A[largest]=pom
        MaxHeapify(A,largest,hs)

def BuildMaxHeap(A,hs):
    hs=len(A)
    for i in range(len(A)//2-1,-1,-1):
        MaxHeapify(A,i,hs)

def HeapSort(A,hs):
    BuildMaxHeap(A,hs)
    for i in range(len(A)-1,0,-1):
        pom=A[0]
        A[0]=A[i]
        A[i]=pom
        hs=hs-1
        MaxHeapify(A,0,hs)
print(L)
startTime=time.clock()
HeapSort(L,hs)
endTime=time.clock()
print(L)
print(endTime-startTime)