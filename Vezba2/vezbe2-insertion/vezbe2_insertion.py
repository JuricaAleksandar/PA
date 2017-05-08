import time
import random
A=[]
startTime=time.clock()
for j in range(1,len(A)):
    key=A[j]
    i=j-1
    while i>=0 and A[i]>key:
        A[i+1]=A[i]
        i=i-1
    A[i+1]=key
endTime=time.clock()
print(endTime-startTime)