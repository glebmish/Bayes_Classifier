from Bayes_Classifier import *

def test():
    train, test = divide(DataSet("..\dataset.txt"), 5)
    bc = BayesClassifier()
    bc.train(train)
    falses_pc, falses_list = bc.check(test)
    assert falses_pc >= 20