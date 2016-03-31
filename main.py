# coding=utf-8
import codecs
from Bayes_Classifier import *

def guess():
    name = raw_input("Write name: ")
    while name != '0':
        print BC.classify(name)
        name = raw_input("Write surname: ")

def cross_validate(classifier, dataset):
    recall = 0.0
    precision = 0.0
    for i in range(10):
        train, test = divide(dataset, i*10, i*10 + 10)
        BC.train(train)
        cur_recall, cur_precision = BC.check(test)
        recall += cur_recall
        precision += cur_precision
    recall /= 10
    precision /= 10
    return recall, precision

dataset = DataSet("dataset_surnames.txt")
BC = BayesClassifier(lambda x: {'last': x[-1], '2nd-last': x[-2], '3rd-last': x[-3]})
print zip(['recall', 'precision'], cross_validate(BC, dataset))
BC.train(dataset)
guess()
