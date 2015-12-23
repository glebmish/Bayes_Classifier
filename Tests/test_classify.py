from Bayes_Classifier import *

training()


def test_classify():
    with open('testing_dataset.txt', 'r') as file:
        for line in file:
            name, type = line.split()
            assert classify(name) == type
