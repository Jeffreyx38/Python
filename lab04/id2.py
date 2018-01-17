#!/usr/bin/python

import sys


if (len(sys.argv) < 2):
    file_path = raw_input("Enter file path or name: ")
    infile = open(file_path, "r")
elif (len(sys.argv) > 2):
    print "Provide only one file to process!"
    exit()
elif (len(sys.argv) == 2):
	infile = open(sys.argv[1], "r")


id=dict()


line = infile.readlines()


for s in line:
	s = s.strip()
	group = s.split(' ', 1)
	id[ group[0] ] = group[1]

keys = []
for key in id.keys():
	keys.append(int (key))

keys.sort()

for key in keys:
	print key, id[ str(key) ]
