####################################
# get

import requests, json

host = "http://www.virustotal.com/"

res = requests.get(host)
res
#<Response [200]>
res.url
#'https://www.virustotal.com/'
res.status_code
#200
res.raise_for_status()
res.content
#b'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="description" content=""><meta name="generator" content="VirusTotal"><tit



#####################################
# get requests with params

my_params = {'id':'gasbugs','pass':'password'}
requests.get(host, params = my_params)
#<Response [200]>



#####################################
# post requests with data
my_data = json.dumps({'id':'gasbugs','pass':'password'})
response = requests.get(host, data = my_data)
