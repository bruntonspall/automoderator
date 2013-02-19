import csv
import sys

r = csv.reader(file(sys.argv[1]))
o = file(sys.argv[2], 'w')

for line in r:
    o.write(line[1]+'. \n')

o.close()

