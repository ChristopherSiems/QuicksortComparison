import pandas
from matplotlib import pyplot
from numpy import log2

data = pandas.read_csv('swap.csv').groupby('input')['time'].mean()
pyplot.plot(data.index, data.values, color = 'C1', label = 'swap')

data = pandas.read_csv('segment.csv').groupby('input')['time'].mean()
pyplot.plot(data.index, data.values, color = 'C2', label = 'segment')

pyplot.title('Mean runtime by input size')
pyplot.xlabel('Input size (# elements in list)')
pyplot.ylabel('Mean runtime (sec)')
pyplot.legend()

pyplot.savefig('fig.png')

pyplot.clf()

x = range(0, 1001)

pyplot.plot(x, (x * log2(x)), color = 'black')
pyplot.title('nlog(n)')
pyplot.xlabel('Input size (# elements in list)')
pyplot.ylabel('Mean runtime')

pyplot.savefig('O.png')