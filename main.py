# coding=utf-8
import codecs
import random
from Bayes_Classifier import *

def guess(classifier):
    name = raw_input("Write name: ")
    while name != '0':
        print classifier.classify(name)
        name = raw_input("Write surname: ")

def cross_validate(classifier, dataset):
    recall = 0.0
    precision = 0.0
    for i in range(10):
        train, test = divide(dataset, i*10, i*10 + 10)
        classifier.train(train)
        cur_recall, cur_precision = classifier.check(test)
        recall += cur_recall
        precision += cur_precision
    recall /= 10
    precision /= 10
    return recall, precision


def shuffle(file_from, file_to):
    lines = []
    for line in open(file_from, 'r'):
        lines.append(line)

    random.shuffle(lines)
    with open(file_to, 'w') as output_to:
        for line in lines:
            output_to.write(line)


def process_surnames():
    dataset = DataSet("dataset_surnames.txt")
    BC = BayesClassifier(lambda x: {'last': x[-1], '2nd-last': x[-2], '3rd-last': x[-3]})
    print zip(['recall', 'precision'], cross_validate(BC, dataset))
    BC.train(dataset)
    guess()


def process_names():
    dataset = DataSet("dataset_names.txt")
    BC = BayesClassifier(lambda x: {'first': x[0], 'last': x[-1]})
    print zip(['recall', 'precision'], cross_validate(BC, dataset))
    BC.train(dataset)
    guess(BC)


process_names()
