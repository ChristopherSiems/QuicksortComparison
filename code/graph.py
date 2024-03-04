import pandas
from matplotlib import pyplot
from numpy import log2

fig, axis1 = pyplot.subplots()

data = pandas.read_csv('swap.csv').groupby('input')['time'].mean()
axis1.plot(data.index, data.values, color = 'C1', label = 'swap')

data = pandas.read_csv('segment.csv').groupby('input')['time'].mean()
axis1.plot(data.index, data.values, color = 'C2', label = 'segment')

axis2 = axis1.twinx()
x = range(1, 1001)

axis2.plot(x, x * log2(x), color = 'black', label = 'nlog(n)')

pyplot.title('Mean runtime by input size')
pyplot.xlabel('Input size (# elements in list)')
axis1.set_ylabel('Mean runtime (sec)')
axis2.set_ylabel('nlog(n)')

lines, labels = axis1.get_legend_handles_labels()
lines2, labels2 = axis2.get_legend_handles_labels()

pyplot.legend(lines + lines2, labels + labels2)

pyplot.savefig('fig.png')