#! /usr/bin/python
# coding=utf-8
# transform_data_id.py

import csv
import sys
import traceback

dataObjectIds = {}

if __name__ == '__main__':
  infile = sys.stdin
  outfile = sys.stdout
  cfgfile = None
  if(len(sys.argv) > 1) :
    cfgfile = open(sys.argv[1], 'rb')
    
  cfgreader = csv.reader(cfgfile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
  reader = csv.reader(infile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
  writer = csv.writer(outfile, delimiter=',', quotechar='"', 
    quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
  for row in cfgreader:
    try:
      key = int(row[0]), int(row[1])
      value = int(row[2])
      dataObjectIds[key] = value
    except ValueError:
      pass
    finally:
      pass
        
  for row in reader:
    try:
      key = int(row[0]), int(row[2])
      dataId = dataObjectIds.get(key, None)
      converted = []
      if dataId != None:
        converted = [dataId, row[1]]
        converted.extend(row[3:])
        writer.writerow(converted)
    except:
		  print >> sys.stderr, row, traceback.format_exc()
