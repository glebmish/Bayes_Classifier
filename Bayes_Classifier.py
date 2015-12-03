def training():
    n = 30
    man = open('man_training.txt', 'r')
    woman = open('woman_training.txt', 'r')
    man_first = man_last = woman_first = woman_last = {}
    for i in range(ord('a'), ord('z') + 1):
        man_first[chr(i)] = man_last[chr(i)] = woman_first[chr(i)] = woman_last[chr(i)] = 0

    for name in man:
        man_first[name[0]] += 1
        man_last[name[-1]] += 1
    for name in woman:
        woman_first[name[0]] += 1
        woman_last[name[-1]] += 1

training()

# P(sex|pair(first, last)) = P(pair(first, last)|sex) * P(sex) / P(pair(first, last)) =
# = ( P(first|sex) * P(sex) / P(first) ) * ( P(last|sex) * P(sex) / P(last) =
# = (man_first[first] / sum(man_first) * 0.5) / ((man_first[first] + woman_first[first]) / (sum(man_first) + sum(woman first)) *
# * (man_last[last] / sum(man_last) * 0.5) / ((man_last[last] + woman_last[last]) / (sum(man_last) + sum(woman last))