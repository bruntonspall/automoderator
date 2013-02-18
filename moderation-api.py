import re
import csv
import json
from collections import defaultdict
from reverend.thomas import Bayes

guesser = Bayes()

def load_csv_to_bayes(filename):
    reader = csv.reader(file(filename))
    reader.next()
    counts = defaultdict(int)
    for line in reader:
        body = line[1]
        if line[2] == "visible":
            status = "visible"
        else:
            status = "moderated"
        clean_body = re.sub("<[^>]*>","",body)
        guesser.train(status, clean_body)


try:
    guesser.load('dataset.dat')
except IOError as e:
    load_csv_to_bayes('good.csv')
    load_csv_to_bayes('bad.csv')
    guesser.save('dataset.dat')


from flask import Flask, request
from flask import render_template
app = Flask(__name__)

@app.route("/moderate")
def moderate():
    if request.args.has_key('callback'):
        wrapper = request.args.get('callback')+"(%s)"
    else:
        wrapper = "%s"
    results = guesser.guess(request.args.get('body'))
    return wrapper % (json.dumps(results))

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
