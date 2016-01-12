from Bayes_Classifier import *

def test():
    bc = BayesClassifier()
    bc.train(DataSet('training_dataset.txt'))
    falses_pc, falses_list = bc.check(DataSet('testing_dataset.txt'))
    assert falses_pc >= 20