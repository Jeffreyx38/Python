#!/usr/bin/python

import sys

if (len(sys.argv) < 2):
	print "file does not exist. Try again" 
	exit()
infile = open(sys.argv[1], "r")

line = infile.readlines()


for str in line:
	total = 0.0
	count = 0
	
	str = str.strip()
	group = str.split(',')
	name = group[0]
	
	for i in range(1, len(group)):
		total += float(group[i])
		count += 1
		average = total/count
	print name, round(average, 1)

