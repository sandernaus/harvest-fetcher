#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

import os
import sys
import yaml
import requests
import calendar
import datetime
import json

# TODO
# 1. Convert to functions
# 2. What happens if .secret file does not exist
# 3. Allow parameters

secret_yaml_file = open(".secret.yml")
parsed_yaml_file = yaml.load(secret_yaml_file, Loader=yaml.FullLoader)

# print ('The user ID is', parsed_yaml_file['userid'])
# print ('The token is', parsed_yaml_file['token'])

userid = str(parsed_yaml_file['userid'])
token = 'Bearer ' + str(parsed_yaml_file['token'])

url = 'https://api.harvestapp.com/api/v2/time_entries'
headers = {'Harvest-Account-ID': userid, 'Authorization': token, 'User-Agent': 'MyApp', 'Content-Type': 'application/json'}
# print (headers)
r = requests.get(url, headers=headers, json={'from': '2020-07-01', 'to': '2020-07-31'})

if r.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /time_entries {}'.format(r.status_code))
jsonResponse = r.json()
# print (json.dumps(r.json(), indent=2))
# print(jsonResponse["time_entries"])
sum = 0
for time_entry in jsonResponse["time_entries"]:
    sum = sum + time_entry["hours"]

print(sum)



# Calculate working days per month
# Calculate wored days per month
# Diff per month

class workingdays_month:
  def __init__(self, month, year):
    self.month = month
    self.year = year

    cal = calendar.Calendar()
    working_days = len([x for x in cal.itermonthdays2(self.year, self.month) if x[0] !=0 and x[1] < 5])
    print ("Total working days this month: " + str(working_days))

    return working_days

month = workingdays_month(7, 2020)

workinghours_month = (workingdays_month(7, 2020) | int * 8 )
print(workinghours_month)
