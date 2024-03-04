from random import randrange
from time import time
import pandas

#Optimzed partition from the book taking pointers, setting pivot to always be the end of the list
def Partition(start, end):
  global A #Defines local A as global A
  p = A[end] #Sets pivot
  l = start - 1
  for i in range(start, end):
    if A[i] <= p:
      l += 1
      (A[l], A[i]) = (A[i], A[l]) #Swaps l and i
  m = l + 1
  (A[m], A[end]) = (A[end], A[m])
  return m

#Optimized QuickSort from the book, takes pointers to front and back of list
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
data.to_csv('swap.csv', index = False)