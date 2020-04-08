#!/usr/bin/env python    
# -*- coding: utf-8 -*-   
# Author: Will

import requests
import json

f = open('post1', encoding='UTF-8')

lines = f.readlines()

url_path = lines[0].strip('\n').split(' ')[1]
host = lines[1].strip('\n').split(' ')[1]
url = 'https://' + host + url_path
print(url)

headers_lines = []
data_lines = []
start_post_data = False
for line in lines[2:]:
    line = line.strip('\n')
    if line == "":
    	start_post_data = True
    if start_post_data == False:
    	headers_lines.append(line)
    elif start_post_data == True:
        data_lines.append(line)

headers = {}
for headers_line in headers_lines:
	key = headers_line.split(': ')[0]
	value = headers_line.split(': ')[1]
	headers[key] = value
print(headers)

data = ""
for i in data_lines:
	data += i

data = eval(data)
request = response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
print(response.text)




