# 🌍 Natural Disaster Tracker

A web app that fetches real-time natural disaster data from **NASA** and **NOAA** public APIs, stores it in a local SQLite database, and displays it on an interactive world map.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-3.x-lightgrey?style=flat-square)
![Plotly](https://img.shields.io/badge/Plotly-Express-purple?style=flat-square)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange?style=flat-square)

---

## What it does

- Pulls earthquake, tsunami, volcano, and wildfire events from NASA EONET and NOAA NGDC
- Saves all events to a local SQLite database with deduplication (no repeated entries on refresh)
- Renders an interactive globe map using Plotly Express — colored by disaster type, sized by magnitude
- Shows a sidebar with live stats and a list of recent events

---

## Data Sources

| Source | Data |
|---|---|
| [NASA EONET v3](https://eonet.gsfc.nasa.gov/docs/v3) | Wildfires |
| [NOAA NGDC](https://www.ngdc.noaa.gov/hazel/hazard-service/api/v1) | Earthquakes, Tsunamis, Volcanoes |

---

## Project Structure

```
project/
├── app.py                  # Flask app — routes and map generation
├── disasters.db            # SQLite database (auto-created on first run)
├── modules/
│   ├── fetch_data.py       # API fetching and data conversion
│   ├── nasa_api.py         # NASA endpoint config
│   ├── noaa_api.py         # NOAA endpoint config
│   ├── natural_disaster.py # NaturalDisaster data class
│   └── database.py         # DB init, read, write
├── templates/
│   └── index.html          # Jinja2 template
└── static/
    └── style.css           # Styles
```

---

## Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/your-username/disaster-tracker.git
cd disaster-tracker
```

**2. Install dependencies**
```bash
pip install flask requests plotly pandas
```

**3. Run the app**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

**5. Fetch data**

Click the **↓ Fetch Data** button on the page. The app will pull current year events from NASA and NOAA and save them to the database. You can click it again at any time — duplicates are automatically skipped.

---

## How it works

1. `fetch_data()` sends GET requests to NASA and NOAA with the current year as a filter
2. `convert()` maps each raw API response to a `NaturalDisaster` object, detecting event type by the fields present in the response
3. `save_disasters()` writes new events to SQLite, skipping any that already exist (matched by title + date)
4. On page load, Flask reads from the database, builds a Plotly scatter geo map server-side, and injects the HTML into the template
5. The page has no client-side JavaScript — everything is rendered by Python on the server

---

## Requirements

- Python 3.10+
- flask
- requests
- plotly
- pandas