#! /usr/bin/python
# coding=utf-8
# validate_history_ai.py

import csv
import sys

if __name__ == '__main__':
  infile = sys.stdin
  outfile = sys.stdout

  reader = csv.reader(infile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
  writer = csv.writer(outfile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
  for row in reader:
    try:
      # check if the number of columns is right.
      if len(row) != 12
        continue;
      # check the format of each column...skipped.
      # check the value range of each column...skipped.
      writer.writerow(row)
    except:
      pass
    finally:
      pass

