#!/usr/bin/python

import sys

if (len(sys.argv)<2):
	print "No file found. Add file as argument!" 
	exit()


id=dict()


infile = open(sys.argv[1], "r")
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
