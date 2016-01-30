from collections import defaultdict
from math import log


def divide(dataset, percent):
    """Divides one dataset on two
    :param dataset: dataset to divide
    :param percent: percent of records that should be stored in the first of returned datsets (with step of 10%)
    :return: two datasets: largest one first
    """
    percent = min(100, percent)
    percent //= 10
    ct = 0
    ds1 = DataSet()
    ds2 = DataSet()

    for record in dataset:
        if ct < percent:
            ds1.add(record)
        else:
            ds2.add(record)
        ct += 1
        if ct == 10:
            ct = 0

    return ds1, ds2


class DataSet:
    def __init__(self, filename = ''):
        self.dataset = []
        self.pos = 0
        self.len = 0
        if filename == '':
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
        """Adds record in dataset"""
        self.dataset.append(record)
        self.len += 1


class Classifier:
    def __init__(self):
        raise Exception("Abstract")

    def train(self, dataset):
        raise Exception("Abstract")

    def check(self, dataset):
        raise Exception("Abstract")

    def classify(self, value):
        raise Exception("Abstract")


class BayesClassifier(Classifier):
    def __init__(self, functor):
        self.features = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.000001)))
        self.get_features = functor
        self.count = defaultdict(lambda: 0.0)

    def train(self, dataset):
        """Collects statistics from training dataset"""
        for value, type in dataset:
            val_features = self.get_features(value)
            for featName in val_features:
                self.features[type][featName][val_features[featName]] += 1
            self.count[type] += 1

        for type in self.features:
            for featName in self.features[type]:
                sum_feat = sum(self.features[type][featName].values())
                for letter in self.features[type][featName]:
                    self.features[type][featName][letter] /= sum_feat
        sum_ct = sum(self.count.values())
        for type in self.count:
            self.count[type] /= sum_ct

    def check(self, dataset):
        """Checks the false percent in testing dataset. Returns false percent and false records"""
        falses_ct = 0
        falses_list = []
        for name, type in dataset:
            cl_type = self.classify(name)
            if cl_type != type:
                falses_ct += 1
                falses_list.append((name, type, cl_type))
        return float(falses_ct) / dataset.len * 100, falses_list

    def classify(self, name):
        """Classifies name based on collected statistics"""
        name = name.lower()
        val_features = self.get_features(name)

        max_type = 'm'
        max_prob = -1000

        for type in self.features:
            prob = log(self.count[type])

            for featName in self.features[type]:
                prob += log(self.features[type][featName][val_features[featName]])
            if max_prob < prob:
                max_prob = prob
                max_type = type

        return max_type
