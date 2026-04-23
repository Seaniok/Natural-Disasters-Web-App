from fetch_data import fetch_data
from datetime import datetime

urls = ["https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1/tsunamis/events",
        "https://www.ngdc.noaa.gov/hazel//hazard-service/api/v1/earthquakes",
        "https://www.ngdc.noaa.gov/hazel//hazard-service/api/v1/volcanoes"]
params = {"year": int(datetime.now().year)}

items_holder = 'items'

