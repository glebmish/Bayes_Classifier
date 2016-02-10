# coding=utf-8
import codecs
from Bayes_Classifier import *

def guess():
    name = raw_input("Write name: ")
    while name != '0':
        print BC.classify(name)
        name = raw_input("Write surname: ")

train, test = divide(DataSet("dataset_surnames.txt"), 80)
BC = BayesClassifier(lambda x: {'last': x[-1], '2nd-last': x[-2], '3rd-last': x[-3]})
BC.train(train)
print BC.check(test)[0]
guess()
