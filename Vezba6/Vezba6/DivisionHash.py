import random
import time

class Data:
    key=0
    literal=0

def ChainedHashInsert(T,x):
    found=False
    try:
        T.index(x.key//10)
        for i in T[x.key//10]:
            if (i.key==x.key):
                i=x
                found=True
        if (found==False):
            T[x.key//10].insert(0,x)
    except:
        L=[]
        L.append(x)
        T.insert(x.key//10,L)

def ChainedHashSearch(T,k):
    try:
        T.index(k//10)
        for i in T[k//10]:
            if (i.key==k):
                return i
    except:
        return 

T=[]
L=[]
for i in range(0,200):
    a=Data()
    a.key=i
    a.literal=random.randint(1,100)
    L.append(a)
start=time.clock()
for i in L: 
    ChainedHashInsert(T,i)
end=time.clock()
print(end-start)
b=ChainedHashSearch(T,10)
print(b)