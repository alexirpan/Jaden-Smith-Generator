from flask import Flask
import mc
app = Flask(__name__)

corpus = mc.init_corpus()
try:
    f = open('tweet_texts', 'r')
    lines = f.readlines()
    f.close()
except:
    print 'could not open file'

for line in lines[1:]:
    mc.update_corpus(corpus, line)
    
@app.route("/")
def hello():
    sentence = [mc.START]
    while sentence[-1] != mc.END:
        sentence.append(mc.sample_from_counts(corpus[sentence[-1]]))
    return ' '.join(word.capitalize() for word in sentence[1:-1])

import os
port = int(os.environ.get('PORT', 5000))
    
if __name__ == '__main__':
    app.run(port=port)