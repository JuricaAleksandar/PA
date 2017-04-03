def SelectionSort(A):
    n = len(A)
    for j in range(n-1):
        iMin = j
        for i in range(j+1,n):
            if(A[i] < A[iMin]):
                iMin=i
        if(iMin != j):
            pom=A[j]
            A[j]=A[iMin]
            A[iMin]=pom