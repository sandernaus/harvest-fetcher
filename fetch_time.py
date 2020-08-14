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

# TODO
# 1. Convert to functions
# 2. What happens if .secret file does not exist
# 3. Allow parameters

secret_yaml_file = open(".secret.yml")
parsed_yaml_file = yaml.load(secret_yaml_file, Loader=yaml.FullLoader)

print 'The user ID is', parsed_yaml_file['userid']
print 'The token is', parsed_yaml_file['token']

userid = str(parsed_yaml_file['userid'])
token = 'Bearer ' + str(parsed_yaml_file['token'])

url = 'https://api.harvestapp.com/api/v2/time_entries'
headers = {'Harvest-Account-ID': userid, 'Authorization': token, 'User-Agent': 'MyApp', 'Content-Type': 'application/json'}
r = requests.get(url, headers=headers)
print r
# if resp.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('GET /time_entries {}'.format(resp.status_code))
# for todo_item in resp.json():
#     print('{} {}'.format(todo_item['id'], todo_item['summary']))
