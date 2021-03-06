import random
import string
from collections import defaultdict

def sample_from_counts(counts):
    total = sum(counts.values())
    s = random.uniform(0, total)
    for word, count in counts.items():
        if s <= count:
            return word
        s -= count
    raise ValueError("should not get here")

def init_corpus():
    return defaultdict(lambda: defaultdict(lambda: 0))

def clean(line):
    # strip out urls
    words = ' '.join(word.capitalize() for word in line.lower().split() if word[:4] != 'http')
    # looks/sounds better without the below, might use again someday though

    # replace punctuation with spaces (deals with case where he uses .... as separators)
    # normalize case as well along the way
    # trans = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    # nopunct = string.translate(line.lower(), trans)
    return words

START = ''
END = None

def update_corpus(corpus, line, weight=1):
    words = [START] + clean(line).split() + [END]
    for i in xrange(len(words) - 1):
        corpus[words[i]][words[i+1]] += weight

def clean_tweets():
    with open('tweet_texts') as f:
        with open('cleaned_tweets', 'w') as f2:
            lines = f.readlines()
            for line in lines:
                print >> f2, clean(line.strip())

if __name__ == '__main__':
    clean_tweets()
