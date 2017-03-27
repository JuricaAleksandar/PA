import time
import numpy as np
import matplotlib.pyplot as plt
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

def CreatePlot(input_data, exec_time, algo_name):
    fig = plt.figure()     
    fig.suptitle(algo_name, fontsize=14, fontweight='bold')    
 
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)       
    ax.set_title('Vreme izvrsenja')
    ax.set_xlabel('Ulaz [n]')    
    ax.set_ylabel('Vreme [ms]')

    ax.plot(input_data, exec_time, '-', color='green')
    
    print(algo_name)
    for i in range(0, len(input_data)):
        print("input_data: ", input_data[i], ", exec_time: ", exec_time[i])

    return fig

def ShowPlot():
    plt.show()
	
    # Sleep for n miliseconds
def Example_fn(n):
    print("Sleeping for ", n, " miliseconds...")
    time.sleep(n/1000) # sleep in miliseconds
    return 
    
    # Profile function Example-fn and create plot
def FirstPlot():
    # Measure exeuction time
    algo_name = "[FirstPlot] Quicksort"
    input_data = []
    exec_time = []
    for n in range(100, 1100, 100):
        L=[]
        for i in range(n):
            L.append(random.randint(1,101))
        start_time = time.clock() # expressed in seconds
        RandomizedQuicksort(L,0,len(L)-1)
        end_time = time.clock()
        exec_time.append((end_time - start_time)*1000) #get miliseconds
        input_data.append(n)

    CreatePlot(input_data, exec_time, algo_name)

    # Profile function Example-fn and create plot	
def SecondPlot():
    # Measure exeuction time
    algo_name = "[SecondPlot] Bucketsort"
    input_data = []
    exec_time = []
    
    for n in range(100, 1100, 100):
    	start_time = time.clock() # expressed in seconds
    	end_time = time.clock()
    	exec_time.append((end_time - start_time)*1000) #get miliseconds
    	input_data.append(n)
    
    CreatePlot(input_data, exec_time, algo_name)


# Profile functions and create plots
FirstPlot()
SecondPlot()

# Show plots
ShowPlot()
