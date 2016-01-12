from collections import defaultdict
from math import log

def divide(self, frequency):
    ct = 0
    ds1 = DataSet()
    ds2 = DataSet()

    for record in self:
        if ct == frequency:
            ds2.add(record)
            ct = 0
        else:
            ds1.add(record)
            ct += 1

    return ds1, ds2

class DataSet:
    def __init__(self, filename = ''):
        self.dataset = []
        self.pos = 0
        self.len = 0
        if filename = '':
            return

        with open(filename, 'r') as file:
            for line in file:
                self.dataset.append(tuple(line.split()))
                self.len += 1

    def __iter__(self):
        return self

    def next(self):
        self.pos += 1
        if self.pos == len(self.dataset):
            raise StopIteration
        else:
            return self.dataset[self.pos - 1]

    def add(self, record):
        self.dataset.append(record)
        self.len += 1

class Classifier:
    def __init__(self):
        pass

    def train(self, dataset):
        pass

    def check(self, dataset):
        pass

    def classify(self, value):
        pass


class BayesClassifier(Classifier):
    def __init__(self):
        self.first = {}
        self.last = {}
        self.count = defaultdict(lambda: 0.0)

    def train(self, dataset):
        for value, type in dataset:
            if type not in self.first:
                self.first[type] = defaultdict(lambda: 0.000001)
                self.last[type] = defaultdict(lambda: 0.0001)
            self.first[type][value[0]] += 1
            self.last[type][value[-1]] += 1
            self.count[type] += 1

        for type in self.first:
            sum_first = sum(self.first[type].values())
            for letter in self.first[type]:
                self.first[type][letter] /= sum_first

            sum_last = sum(self.last[type].values())
            for letter in self.last[type]:
                self.last[type][letter] /= sum_last

        ct_sum = sum(self.count.values())
        for type in self.count:
            self.count[type] /= ct_sum

    def check(self, dataset):
        falses_ct = 0
        falses_list = []
        for name, type in dataset:
            cl_type = self.classify(name)
            if cl_type != type:
                falses_ct += 1
                falses_list.append((name, type, cl_type))
        return float(falses_ct) / dataset.len * 100, falses_list

    def classify(self, name):
        name = name.lower()

        max_type = 'm'
        max_prob = 0

        for type in self.first:
            prob = log(self.first[type][name[0]]) + log(self.last[type][name[-1]]) + log(self.count[type])
            if max_prob < prob:
                max_prob = prob
                max_type = type

        return max_type
