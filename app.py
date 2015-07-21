from flask import Flask, render_template, url_for, request

import copy
import mc
import os
import sys


app = Flask(__name__)


# Create the first model by calling this function
def jaden_corpus():
    corpus = mc.init_corpus()
    lines = []

    with open('tweet_texts', 'r') as f:
        lines = f.readlines()

    for line in lines[1:]:
        mc.update_corpus(corpus, line)
    return corpus


# Create the second by calling jaden_corpus(), then pass the returned
# corpus to this function to incorporate the Bible
def bible_update(corpus):
    with open('AV1611Bible.txt', 'r') as f:
        for line in f:
            # The weight is chosen sucn that (# words) * (weight) is the same
            # between the Bible and the Jaden Smith tweets, assuming every word
            # from Jaden Smith gets weight 1
            # The true number is slightly different, I did some hand-tweaking
            # here to get nicer sounding results
            mc.update_corpus(corpus, line, weight=0.012)
    return corpus

# a/a+b, b/a+b
# b+a/2a, a+b/2b


@app.route("/")
def hello():
    message = ' '
    while message == ' ':
        sentence = [mc.START]
        while sentence[-1] != mc.END:
            sentence.append(mc.sample_from_counts(corpus[sentence[-1]]))
        message = ' '.join(word.capitalize() for word in sentence[1:-1])

    return render_template('index.html', message=message)

import os
debug = True
host = '127.0.0.1' if debug else '0.0.0.0'
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
#    app.run(host=host, port=port)
    import dill
    with open('jaden_model', 'w') as f:
        dill.dump(jaden_corpus(), f)

    with open('jaden_bible_model', 'w') as f:
        dill.dump(bible_update(jaden_corpus()), f)
