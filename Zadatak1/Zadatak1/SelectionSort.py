def SelectionSort(A):
	for j in range(0,len(A)-1,1):
		iMin=j
		for i in range(j+1,len(A),1):
			if(A[i]<A[iMin]):
				iMin=i
		if(iMin!=j):
			pom=A[j]
			A[j]=A[iMin]
			A[iMin]=pom