from datetime import datetime

urls = ["https://eonet.gsfc.nasa.gov/api/v3/events?"]
params = {"category": "wildifires", "start": f"{datetime.now().year}-01-01"}

items_holder = 'events'

# response = requests.get(url)
# print(f"Status Code: {response.status_code}")

# events = response['events']

# disasters = []
# for event in events:
#     geometry = event['geometries'][0]
#     lon = geometry['coordinates'][0]
#     lat = geometry['coordinates'][1]
#     date = geometry['date']
#     title = event['title']
    
#     nd_title = event['categories'][0]['title']
#     if nd_title ==  'Wildfires':
#         obj = Wildfire(title, lon, lat, date)
#         disasters.append(obj)
    
    
    
    
# title = 'Active natural disasters - last 30 days'
# fig = px.scatter_map(
#     lat=[d.lat for d in disasters],
#     lon=[d.lon for d in disasters],
#     hover_name=[d.title for d in disasters]
# )
# fig.show()

