import requests
import os
import json

try:
    print("Shamia's ip tracker")
    ip_tracker = input('enter an ip address= ')
    api = 'http://ip-api.com/json/'
    res = requests.get(api + ip_tracker)
    data = res.json()                                          
    os.system('clear')                                          
    print(f"""Ip: {data['query']}""")                           
    print(f"""Country: {data['country']}""")
    print(f"""Country Code: {data['countryCode']}""")
    print(f"""Region: {data['regionName']}""")
    print(f"""City: {data['city']}""")
    print(f"""Zip Code: {data['zip']}""")
    print(f"""Latitude: {data['lat']}""")
    print(f"""Longitude: {data['lon']}""")
    print(f"""Time Zone: {data['timezone']}""")
    print(f"""Internet Service Provider: {data['isp']}""")
    print(f"""Organization: {data['org']}""")
    print(f"""AS: {data['as']}""")    
except:
    print("invalid ip address!.")
