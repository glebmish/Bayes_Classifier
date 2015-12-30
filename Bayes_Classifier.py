from collections import defaultdict


class DataSet:
    def __init__(self, filename):
        self.dataset = []
        self.pos = 0
        self.len = 0
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

    # def divide(self, border):
    #   lDs = DataSet()
    #    rDs = DataSet()


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
                self.last[type] = defaultdict(lambda: 0.000001)
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
        ct = 0
        falses = []
        for name, type in dataset:
            cl_type = self.classify(name)
            if cl_type != type:
                ct += 1
                falses.append((name, type, cl_type))
        return float(ct) / dataset.len * 100, falses

    def classify(self, name):
        name = name.lower()

        max_type = 'm'
        max_prob = 0

        for type in self.first:
            prob = self.first[type][name[0]] * self.last[type][name[-1]] * self.count[type]
            if max_prob < prob:
                max_prob = prob
                max_type = type

        return max_type
