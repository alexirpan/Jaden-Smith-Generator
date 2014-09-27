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
    # strip out urls
    words = ' '.join(word for word in line.split() if word[:4] != 'http')
    # replace punctuation with spaces (deals with case where he uses .... as separators)
    # normalize case as well along the way
    trans = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    nopunct = string.translate(line.lower(), trans)
    return words

START = ''
END = None

def update_corpus(corpus, line):
    words = [START] + clean(line).split() + [END]
    for i in xrange(len(words) - 1):
        corpus[words[i]][words[i+1]] += 1
