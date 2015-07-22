#! /bin/env python
# coding=utf-8
# remove_duplicate.py

import csv
import sys

currentRow = None
def duplicate(row):
  global currentRow

  result = True
  if(currentRow == None):
    result = False
  else:
    for i, j in zip(row, currentRow):
      if i != j:
        result = False
        break
    currentRow = row
  return result

if __name__ == '__main__':
  infile = sys.stdin
  outfile = sys.stdout
  if(len(sys.argv) > 1) :
    infile = open(sys.argv[1], 'rb')
    
  reader = csv.reader(infile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
  writer = csv.writer(outfile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
  for row in reader:
    if(not duplicate(row)):
      writer.writerow(row)
