import requests
from modules.natural_disaster import NaturalDisaster

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

        # Wykryj typ
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

        try:
            match obj.type:
                case "Tsunami":
                    obj.lat   = element['latitude']
                    obj.lon   = element['longitude']
                    obj.date  = f"{element.get('day','?')}-{element.get('month','?')}-{element.get('year','?')}"
                    height    = element.get('maxWaterHeight')
                    obj.mag   = round((height / 30) * 100, 1) if height else 0
                    obj.title = f"Tsunami: {element.get('locationName','?')}, {element.get('country','?')}"
                    if "deathsTotal" in element:
                        obj.info = f"Death Count: {element['deathsTotal']}"

                case "Volcanoe":
                    obj.lat   = element['latitude']
                    obj.lon   = element['longitude']
                    obj.date  = f"{element.get('day','?')}-{element.get('month','?')}-{element.get('year','?')}"
                    obj.mag   = element.get('vei', 0) or 0
                    obj.title = f"Volcano Eruption: {element.get('locationName','?')}, {element.get('country','?')}"
                    if "deathsTotal" in element:
                        obj.info = f"Death Count: {element['deathsTotal']}"

                case "Earthquake":
                    obj.lat   = element['latitude']
                    obj.lon   = element['longitude']
                    obj.date  = f"{element.get('day','?')}-{element.get('month','?')}-{element.get('year','?')}"
                    obj.mag   = element.get('eqMagnitude', 0) or 0
                    obj.title = f"Earthquake: {element.get('locationName','?')}"
                    if "deathsTotal" in element:
                        obj.info = f"Death Count: {element['deathsTotal']}"

                case "Wildfire":
                    geometries = element.get('geometries', [])
                    if not geometries:
                        continue
                    geometry  = geometries[0]
                    coords    = geometry.get('coordinates', [None, None])
                    obj.lon   = coords[0]
                    obj.lat   = coords[1]
                    obj.date  = geometry.get('date', '')
                    obj.mag   = geometry.get('magnitudeValue', 0) or 0
                    obj.title = element.get('title', 'Wildfire')
                    obj.info  = element.get('description', '')

            # Pomiń jeśli brak współrzędnych
            if obj.lat is None or obj.lon is None:
                continue

            results.append(obj)

        except Exception as e:
            print(f"[convert] Pominięto rekord: {e}")
            continue

    return results
                 
                
    
            
            
            
            
        