#! /bin/env python
# coding=utf-8
# remove_duplicate.py

import csv
import sys

if __name__ == '__main__':
  leftTableIn = sys.stdin
  rightTableIn = open(sys.argv[1], 'rb')
  outfile = sys.stdout
    
  leftReader = csv.reader(leftTableIn, delimiter=',', 
    quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
  rightReader = csv.reader(rightTableIn, delimiter=',', 
    quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
  writer = csv.writer(outfile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)

  try:
    r1 = leftReader.__next__()
    r2 = rightReader.__next__()
    while True:    
      key1 = (r1[0], r1[2])
      key2 = (r1[0], r1[1])
      if key1 < key2:
        r1 = leftReader.__next__()
      elif key1 > key2:
        r2 = rightReader.__next__()
      else:
        row = []
        row.extend(r1)
        row.append(r2[2])
        writer.writerow(row)
  except StopIteration:
    pass;
