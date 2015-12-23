from Bayes_Classifier import *

training()
while True:
    name = raw_input("Write name: ")
    type = classify(name)
    if type == 'm':
        print("man")
    elif type == 'w':
        print("woman")