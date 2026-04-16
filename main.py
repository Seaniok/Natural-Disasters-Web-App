import requests
import plotly.express as px
from natural_disaster import *

url = "https://eonet.gsfc.nasa.gov/api/v2.1/events?days=7"

r = requests.get(url)
print(f"Kod stanu: {r.status_code}")

response = r.json()
events = response['events']

disasters = []
for event in events:
    geometry = event['geometries'][0]
    lon = geometry['coordinates'][0]
    lat = geometry['coordinates'][1]
    date = geometry['date']
    title = event['title']
    
    nd_title = event['categories'][0]['title']
    if nd_title == 'Wildfires':
        obj = Wildfire(title, lon, lat, date)
        disasters.append(obj)
    elif nd_title == 'Severe Storms':
        obj = Storm(title, lon, lat, date)
        disasters.append(obj)
    
    
    
    
title = 'Active natural disasters - last 7 days'
fig = px.scatter_map(
    lat=[d.lat for d in disasters],
    lon=[d.lon for d in disasters],
    hover_name=[d.title for d in disasters]
)
fig.show()

