import json
import functools 
from collections import defaultdict
from itertools import repeat

def add(i,j): 
    return i+j

f = file('text1.txt')
text = f.read()
charsToReplace = ['\n', ':']
replacedText = functools.reduce(lambda i,j: i.replace(j,''), charsToReplace, text)
lines = [line.strip() for line in replacedText.split('.')]

d = defaultdict(lambda: defaultdict(int))
combinations = functools.reduce(add, [zip(["*BEGIN*"]+line.split(' '), line.split(' ')+["*END*"]) for line in lines])
for (k,v) in combinations: 
    d[k][v] = d[k][v]+1

combos = dict([(k,reduce(add, [list(repeat(ik,iv)) for ik,iv in v.iteritems()])) for (k,v) in d.iteritems()])
f = file('words.json', 'w')
json.dump(combos, f)
