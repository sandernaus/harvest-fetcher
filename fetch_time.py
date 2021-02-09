#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...

   TODO:
   - Add proper error handling
   - Update documentation
   - print nice table output
   - refactor variable name
"""

import yaml
import requests
import calendar

def main(year:int=2020,file='.secret.yml'):

    secret_file = load_secret(
        file = file
    )

    months=[1,2,3,4,5,6,7,8,9,10,11,12]

    for i in months:
        time_entries = get_time_entries(
            userid = str(secret_file['userid']),
            token =  str(secret_file['token']),
            month = i,
            year = year
        )

        workingdays_month = workinghours_month(
            month = i,
            year = year
        )

        print('Worked hours ' + str(time_entries))

        print('Actual working hours ' + str(workingdays_month))

        print('Difference ' + str(time_entries-workingdays_month))

def load_secret(file):
    try:
        secret_yaml_file = open(file)

        parsed_yaml_file = yaml.load(secret_yaml_file, Loader=yaml.FullLoader)

        return parsed_yaml_file

    except:
        print ('Secret file not found')

def get_time_entries(userid:str,token:str,month:int,year:int):

    token = 'Bearer ' + token

    get_last_day = calendar.monthrange(year, month)[1]

    if len(str(month)) == 1:
        month = '0' + str(month)
    else:
        month = str(month)

    year = str(year)

    first_day = year + '-' + month + '-01'
    last_day = year + '-' + month + '-' + str(get_last_day)

    url = 'https://api.harvestapp.com/api/v2/time_entries'
    headers = {'Harvest-Account-ID': userid, 'Authorization': token, 'User-Agent': 'MyApp', 'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers, json={'from': first_day, 'to': last_day})

    if r.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /time_entries {}'.format(r.status_code))
    jsonResponse = r.json()
    sum = 0
    for time_entry in jsonResponse["time_entries"]:
        sum = sum + time_entry["hours"]

    return sum

def workinghours_month(month, year):

    cal = calendar.Calendar()
    working_days = len([x for x in cal.itermonthdays2(year, month) if x[0] !=0 and x[1] < 5])

    workinghours_month = (working_days * 8 )

    return workinghours_month

if __name__ == "__main__":
    main()
