import re
import csv
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



import sys
inp = 'notend'
while inp != 'END':
    print "Word >"
    inp = raw_input()
    print "Word has moderate value: ",guesser.guess(inp)

