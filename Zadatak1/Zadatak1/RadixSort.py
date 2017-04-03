import math

def RadixSort(A):
    divider=10;
    pos=1
    while True:
        buckets=[list() for i in range(10)]
        for i in A:
            buckets[math.floor((i%divider)/pos)].append(i)
        if len(A)==len(buckets[0]):
            return
        A=[]
        for i in buckets:
            for j in i:
                A.append(j)
        divider=divider*10
        pos=pos*10