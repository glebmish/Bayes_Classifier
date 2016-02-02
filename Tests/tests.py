from Bayes_Classifier import *
import os


def test_falses():
    current_path = os.path.dirname(os.path.abspath(__file__))
    train, test = divide(DataSet(current_path + "\..\dataset_names.txt"), 80)
    bc = BayesClassifier(lambda x: {'first': x[0], 'last': x[-1]})
    bc.train(train)
    falses_pc, falses_list = bc.check(test)
    assert falses_pc < 22


def test_divide():
    percent = 1
    current_path = os.path.dirname(os.path.abspath(__file__))
    dataset = DataSet(current_path + "\..\dataset_names.txt")

    ds1, ds2 = divide(dataset, percent)
    assert ds1.len - 5 < dataset.len / 100 * percent < ds1.len + 5
    assert ds2.len == dataset.len - ds1.len
