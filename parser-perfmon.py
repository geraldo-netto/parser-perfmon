#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import glob

if len(sys.argv) < 2:
    print("Usage: %s <directory>" % sys.argv[0])
    sys.exit(0)

elif sys.argv[1] and not os.path.isdir(sys.argv[1]):
	print ("invalid path: %s" % os.path.isdir(sys.argv[1]))
    sys.exit(1)


paths = glob.glob(sys.argv[1] + os.sep + '*.csv')
old_name = ''

for path in paths:
	file = open(path, 'r').readlines()
	name = path.split('.')[0].split('\\')[-1].split('_')[0]
	header = file[0].replace('","','";"').replace('"', '').replace('\\\\' + name + '\\', '')
	header = header.replace('(PDH-CSV 4.0) (E. South America Standard Time)(180)', 'date')

	with open(name + '.csv', 'a') as file_csv:
		if old_name != name:
			file_csv.write(header)

		for line in file[1:]:
			line_updated = line.replace('","',';').replace('"', '').replace('.',',')
			date = line_updated[:20]
			# 24? 25? 26?
			content = line_updated[24:].replace(' ', '')
			dd = date[:7][3:5]
			mm = date[:4][:2]
			yyyy = date[6:-4]

			file_csv.write(dd + '/' + mm + '/' + yyyy + ';' + content)

		old_name = name

	file_csv.close()
