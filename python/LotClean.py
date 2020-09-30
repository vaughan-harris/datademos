#!/usr/bin/env python
# coding: utf-8

# # Collect Data from National Lottery
# ## Set For Life

import urllib.request
from time import sleep
import os
import re


# Cleaner Script
def cleaner(contents):
    content_new = contents

    content_new = re.sub(r'<script.*?/script>', r'', content_new, flags=re.S)
    content_new = re.sub(r'<footer.*?/html>', r'', content_new, flags=re.S)
    content_new = re.sub(r'(\r\n){2}', r'', content_new, flags=re.S)
    content_new = re.sub(r'<meta.*?/>', r'', content_new, flags=re.S)
    content_new = re.sub(r'<link.*?/>', r'', content_new, flags=re.S)

    #content_new = re.sub(r'\s{2,50}', r'', content_new, flags=re.S)
    return("TBALL "+content_new)

dirname = "/home/vaughan/Documents/Data/datacollection_demo/data/NationalLottery/euromillions/Breakdown/"

for filename in os.listdir(dirname):
	print(dirname+filename)
	with open(dirname+filename, 'r') as f:
		content = f.read()
		content_new=cleaner(content)
		f = open(dirname+filename+"_a", "w")
		f.write(content_new)
		f.close()

