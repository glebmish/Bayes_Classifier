from Bayes_Classifier import *

BC = BayesClassifier()
BC.train(DataSet('training_dataset.txt'))
print BC.check(DataSet('testing_dataset.txt'))
while True:
    name = raw_input("Write name: ")
    type = BC.classify(name)
    if type == 'm':
        print("man")
    elif type == 'w':
        print("woman")