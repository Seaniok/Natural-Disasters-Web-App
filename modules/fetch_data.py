import requests
from natural_disaster import NaturalDisaster

def fetch_data(urls: list, params, items_holder):
    elements = []
    for url in urls:
        try:
            response = requests.get(url, params=params)
            status_code = response.status_code
            element = response.json()
            elements.append(element[items_holder])
            print(f"Status Code: {status_code}")
        except Exception as e:
            print(f"Wyjebalo cos: {e}")
    
    return elements

def convert(elements):
    results = []    
    for element in elements:
        obj = NaturalDisaster()
        # Type
        if "oceanicTsunami" in element.keys():
            obj.type = "Tsunami"
        elif "timeErupt" in element.keys():
            obj.type = "Volcanoe"
        elif "eqMagMw" in element.keys():
            obj.type = "Earthquake"
        elif "categories" in element.keys():
            obj.type = "Wildfire"
        else:
            continue

        match obj.type:
            case "Tsunami":
                obj.lat = element['latitude']
                obj.lon = element['longitude']
                obj.date = f"{element['day']}-{element['month']}-{element['year']}"
                obj.mag = (element['maxWaterHeight'] / 30) * 100
                obj.title = f"Tsunami: {element['locationName']}, {element['country']}"
                if "deathsTotal" in element.keys():
                    obj.info = f"Death Count: {element['deathsTotal']}"
            
            case "Volcanoe":
                obj.lat = element['latitude']
                obj.lon = element['longitude']
                obj.date = f"{element['day']}-{element['month']}-{element['year']}"
                obj.mag = element['vei'] # Zrób jeszcze przeliczenie !!
                obj.title = f"Volcanoe Eruption: {element['locationName']}, {element['country']}"
                if "deathsTotal" in element.keys():
                    obj.info = f"Death Count: {element['deathsTotal']}"
            
            case "Earthquake":
                obj.lat = element['latitude']
                obj.lon = element['longitude']
                obj.date = f"{element['day']}-{element['month']}-{element['year']}"
                obj.mag = element['eqMagnitude'] # Zrób jeszcze przeliczenie !!!
                obj.title = f"Earthquake: {element['locationName']}"
                if "deathsTotal" in element.keys():
                    obj.info = f"Death Count: {element['deathsTotal']}"
            
            case "Wildfire":
                geometry = element['geometries'][0]
                obj.lat = geometry['coordinates'][1]
                obj.lon = geometry['coordinates'][0]
                obj.date = geometry['date']
                obj.mag = geometry['magnitudeValue']
                obj.title = element['title']
                obj.info = element['description']
            
            
            
        results.append(obj)
    
    return results
                 
                
    
            
            
            
            
        