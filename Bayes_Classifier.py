from collections import defaultdict

first = {}
last = {}
count = defaultdict(lambda: 0.0)

def training():
    for line in open('training_dataset.txt', 'r'):
        value, type = line.split()
        if type not in first:
            first[type] = defaultdict(lambda: 0.000001)
            last[type] = defaultdict(lambda: 0.000001)
        first[type][value[0]] += 1
        last[type][value[-1]] += 1
        count[type] += 1

    for type in first:
        sum_first = sum(first[type].values())
        for letter in first[type]:
            first[type][letter] /= sum_first

        sum_last = sum(last[type].values())
        for letter in last[type]:
            last[type][letter] /= sum_last


def classify(name):
    name = name.lower()
    max_type = 'm'

    max_prob = 0
    for type in first:
        prob = first[type][name[0]] * last[type][name[-1]] * (count[type] / sum(count.values()))
        print(type, prob)
        if max_prob < prob:
            max_prob = prob
            max_type = type

    return max_type

training()
while True:
    name = raw_input("Write name: ")
    type = classify(name)
    if type == 'm':
        print("man")
    elif type == 'w':
        print("woman")