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

BC = BayesClassifier()
BC.train(DataSet('training_dataset.txt'))
print BC.check(DataSet('testing_dataset.txt'))
guess()