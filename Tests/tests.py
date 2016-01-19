from Bayes_Classifier import *
import os

def test_falses():
    current_path = os.path.dirname(os.path.abspath(__file__))
    train, test = divide(DataSet(current_path + "\..\dataset.txt"), 80)
    bc = BayesClassifier()
    bc.train(train)
    falses_pc, falses_list = bc.check(test)
    assert falses_pc < 20

def test_divide():
    current_path = os.path.dirname(os.path.abspath(__file__))
    dataset = DataSet(current_path + "\..\dataset.txt")

    ds1, ds2 = divide(dataset, 60)
    assert ds1.len - 5 < dataset.len / 100 * 60 < ds1.len + 5 and ds2.len - 5 < dataset.len / 100 * 40 < ds2.len + 5
