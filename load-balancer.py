from random import random
from bisect import bisect

def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random() * total
    i = bisect(cum_weights, x)
    return values[i]


for i in range(100):
    print("i:",i," value",weighted_choice([("OptionA",90), ("OptionB",10)]))
    i+=1
