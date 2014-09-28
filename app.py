from flask import Flask, render_template
import mc
app = Flask(__name__)

corpus = mc.init_corpus()
lines = []
try:
    f = open('tweet_texts', 'r')
    lines = f.readlines()
    f.close()
except:
    print 'could not open file'

for line in lines[1:]:
    mc.update_corpus(corpus, line)

# a/a+b, b/a+b
# b+a/2a, a+b/2b
    
try:
    f = open('AV1611Bible.txt', 'r')
    for line in f:
        # a weight that roughly corresponds to 25% of words from king james bible
        # (assuming word distributions are uniform between the two, This isn't true)
        mc.update_corpus(corpus, line, weight=0.007)
    f.close()
except:
    print 'could not open bible'
    
@app.route("/")
def hello():
    sentence = [mc.START]
    while sentence[-1] != mc.END:
        sentence.append(mc.sample_from_counts(corpus[sentence[-1]]))
    message = ' '.join(word.capitalize() for word in sentence[1:-1])
    return render_template('index.html', message=message)

import os
debug = False
host = '127.0.0.1' if debug else '0.0.0.0'
port = int(os.environ.get('PORT', 5000))
    
if __name__ == '__main__':
    app.run(host=host, port=port)
