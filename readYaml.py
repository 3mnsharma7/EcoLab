#!/usr/local/bin/python2.7
\
import yaml

with open ('startcommands.yaml') as f:
	doc = yaml.load(f)
        print "doc : ", doc
        print "Type of doc : ", type(doc)

for k, v in doc.items():
	print "Key - Value Pair : ", k, v
	for index, item in enumerate(v):
		print "value [", index, "]", " : ", item 
