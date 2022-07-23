import os
import signal
from flask import Flask

generator = None

try:
    from buzz import generator
except:
    import random

    buzz = ('continuous testing', 'continuous integration', 'continuous deployment', 'continuous improvement', 'devops')
    adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
    adverbs = ('remarkably', 'enormously', 'substantially', 'significantly', 'seriously')
    verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')


    def sample(l, n=1):
        result = random.sample(l, n)
        if n == 1:
            return result[0]
        return result


    def generate_buzz_worker():
        buzz_terms = sample(buzz, 2)
        phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs), sample(verbs), buzz_terms[1]])
        return phrase.title()

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))


@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz() if generator else generate_buzz_worker()
    page += '</h1></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT')) # port 5000 is the default
