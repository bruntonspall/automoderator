import json
import functools 
from collections import defaultdict
from itertools import repeat, izip
import re
import sys

def add(i,j): 
    return i+j

f = file(sys.argv[1])
text = f.read()
charsToReplace = ['\n', ':']
replacedText = functools.reduce(lambda i,j: i.replace(j,''), charsToReplace, text)
replacedText = re.sub("<[^>]*>", "", replacedText)
d = defaultdict(lambda: defaultdict(int))
lines = [line.strip()+'.' for line in replacedText.split('.') if line.strip() != '']
beginnings = []
for line in lines:
    words = line.split(' ')
    if len(words) > 2:
        beginnings.append(words[0]+" "+words[1])
        triples = izip(words, words[1:], words[2:])
        for (one, two, nxt) in triples:
            d[one+" "+two][nxt] += 1

combos = dict([(k,reduce(add, [list(repeat(ik,iv)) for ik,iv in v.iteritems()])) for (k,v) in d.iteritems()])
combos["*BEGIN*"] = beginnings
print "Writing to file ",sys.argv[2]
f = file(sys.argv[2], 'w')
json.dump(combos, f, indent=2)
