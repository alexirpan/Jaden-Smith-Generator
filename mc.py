import random
from collections import defaultdict

def sample_from_counts(counts):
    total = sum(counts.values())
    s = random.randint(1, total)
    for word, count in counts.items():
        if s <= count:
            return word
        s -= count
    raise ValueError("should not get here")

def init_corpus():
    return defaultdict(lambda: defaultdict(lambda: 0))

import string

def clean(line):
    # normalize case
    # strip out urls and punctuation
    # TODO exception for hashtags and @ for twitter users?
    return ''.join(ch for ch in line.lower() if ch not in string.punctuation)

START = ''
END = None

def update_corpus(corpus, line):
    words = [START] + clean(line).split() + [END]
    for i in xrange(len(words) - 1):
        corpus[words[i]][words[i+1]] += 1
