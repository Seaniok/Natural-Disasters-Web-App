from datetime import datetime

urls = ["https://eonet.gsfc.nasa.gov/api/v3/events?"]
params = {"category": "wildfires", "start": f"{datetime.now().year}-01-01"}

items_holder = 'events'