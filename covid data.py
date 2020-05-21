# importing libraries

# importing libraries

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np
import re


extract_contents = lambda row: [x.text.replace('\n', '') for x in row]#

SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed',
				'Foreign-Confirmed','Cured','Death']

URL = 'https://www.mohfw.gov.in/'
response = requests.get(URL).content #it gets whole html template file of url we provided
soup = BeautifulSoup(response, 'html.parser')
print(soup.tr.find_all('th'))
header = extract_contents(soup.tr.find_all('th'))
print(header)
ab=header[2][:21]#bcz bydefault 3rd column name is too large so we reduce by using this
header[2]=ab

# print(header)

stats = []
all_rows = soup.find_all('tr')
print(all_rows[2])
print(extract_contents(all_rows[2].find_all('td')))

# for row in range(0,len(all_rows)):
# 	stat = extract_contents(all_rows[row].find_all('td'))
# 	if stat:
# 		if len(stat) == 5 or len(stat) ==6:
# 			stats.append(stat)
#
# table = tabulate(stats, headers=header)
# # print(table)
# a=open('E:/covid.pdf','w+')
# a.write(table)
# os.startfile('E:/covid.pdf')