from Bayes_Classifier import *


def guess():
    name = raw_input("Write name: ")
    while name != '0':
        type = BC.classify(name)
        if type == 'm':
            print("man")
        elif type == 'w':
            print("woman")
        name = raw_input("Write name: ")

train, test = divide(DataSet("dataset.txt"), 80)
BC = BayesClassifier(lambda x: {'first': x[0], 'last': x[-1]})
BC.train(train)
print BC.check(test)
guess()
