L=[3,7,9,2,1,7,8,9,4,6]
n=6
def LinSearch(A,a):
    for i in range(len(A)):
       if A[i]==a:
            return i
f=LinSearh(L,n)
print(f)