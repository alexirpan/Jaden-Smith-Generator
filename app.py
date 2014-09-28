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
    
@app.route("/")
def hello():
    if not lines:
        return 'lines was never set'
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
