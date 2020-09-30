import csv
import numpy

#added
import os
import pandas as pd


dataset = os.path.join('..', 'DATASETS', 'pima-indians-diabetes.data')


# with numpy (code given)
raw_data = open(dataset, 'rt')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
# print(data, data.shape)

# with numpy bis
raw_data = open(dataset, 'rt')
data = numpy.loadtxt(raw_data, delimiter=",")
# print(data, data.shape)

# with pandas
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data_pd = pd.read_csv(dataset, names=names)
print(data_pd, data_pd.shape)

