# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:18:02 2017

@author: Samvat
"""
import requests as req
import pandas as pd

df = pd.read_csv('cities.csv')
cities = df['Cities'].values

df_length = len(cities)

out = pd.DataFrame(columns = ('cityname','latitude', 'longitude'))

for x in range(df_length):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + cities[x]
    response = req.get(url)
    res_json_payload = response.json()
    cityname = cities[x]
    latitude = res_json_payload['results'][0]['geometry']['location']['lat']
    longitude = res_json_payload['results'][0]['geometry']['location']['lng']
    out = out.append({'cityname': cityname,'latitude': latitude, 'longitude': longitude}, ignore_index=True)

print(out)


out.to_csv('result.csv', sep=',', encoding='utf-8')