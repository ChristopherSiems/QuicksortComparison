# Quicksort Comparison

Comparing the runtimes of 2 different Quicksort implementations.

## How To

1. Run `quicksort_swap.py`, this will save `swap.csv` which contains the runtimes for 10,000 lists of length 1 to 1000 sorted using the quicksort method in 'Algorithms' by Jeff Erickson.

2. Run `quicksort_segment.py`, this will save `segment.csv` which contains the runtimes of 100,000 lists of length 1 to 1000 sorted using the quicksort method as taught by Prof. Tseng of Clark University.

3. Run `graph.py` this will produce and save `fig.png` which graphs the mean runtimes of each quicksort by the size of the input along side the theoretical runtime of $\cal{O}(n \log(n))$.
