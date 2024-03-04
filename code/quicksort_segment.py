from random import randrange
from time import time
import pandas

#Optimized partition from class, taking pointers
def Partition(start, end):
  global A
  AL = []
  AR = []
  for i in range(start, end):
    if A[i] < A[end]: #Pivot at end
      AL += [A[i]]
    else:
      AR += [A[i]]
  A[start : end + 1] = AL + [A[end]] + AR #Setting slice of global A to partitioned sublist
  return start + len(AL) #Returning the pivot's location in the global A

#Optimized QuickSort from class, taking pointers
def QuickSort(start, end):
  if start < end:
    r = Partition(start, end)
    QuickSort(start, r - 1)
    QuickSort(r + 1, end)

#Tracks runtime with 100000 different lists
data = pandas.DataFrame(columns = ['input', 'time'])
for i in range(1, 1001):
  for j in range(0, 100):
    A = [randrange(-1000, 1001) for k in range(0, i)]
    start = time()
    QuickSort(0, i - 1)
    end = time()
    data.loc[len(data.index)] = [i, end - start]
data.to_csv('segment.csv', index = False)