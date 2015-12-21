from collections import defaultdict

first = {}
last = {}
count = defaultdict(lambda: 0)

def training():
    for line in open('training_dataset.txt', 'r'):
        value, type = line.split()
        if type not in first:
            first[type] = defaultdict(lambda: 0.0)
            last[type] = defaultdict(lambda: 0.0)
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


def guess(name):
    name = name.lower()
    max_type = 'm'
    max_prob = 0
    for type in first:
        print(name[0], name[-1], first[type][name[0]], first[type][name[-1]])
        prob = first[type][name[0]] * last[type][name[-1]] * (count[type] / sum(count.values()))
        if max_prob < prob:
            max_prob = prob
            max_type = type

    return max_type

training()
print(first)
print(last)
while True:
    name = raw_input("Write name: ")
    type = guess(name)
    if type == 'm':
        print("man")
    elif type == 'w':
        print("woman")