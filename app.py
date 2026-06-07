from flask import Flask, render_template, redirect, url_for
from modules.database import init_db, save_disasters, get_disasters, get_stats
from modules.fetch_data import fetch_data, convert
import modules.nasa_api as nasa
import modules.noaa_api as noaa
import plotly.express as px
import pandas as pd

app = Flask(__name__)


def build_map(disasters: list) -> str:
    if not disasters:
        return "<p class='no-data'>Brak danych. Kliknij 'Pobierz dane' żeby zaciągnąć zdarzenia.</p>"

    df = pd.DataFrame(disasters)
    df = df.dropna(subset=['lat', 'lon'])

    COLOR_MAP = {
        "Earthquake": "#f87171",
        "Tsunami":    "#38bdf8",
        "Volcanoe":   "#fb923c",
        "Wildfire":   "#fbbf24",
    }

    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lon",
        color="type",
        color_discrete_map=COLOR_MAP,
        hover_name="title",
        hover_data={"date": True, "mag": True, "info": True, "lat": False, "lon": False},
        size="mag",
        size_max=20,
        projection="natural earth",
    )

    fig.update_layout(
        autosize=True,
        paper_bgcolor="#0a0c10",
        plot_bgcolor="#0a0c10",
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            bgcolor="#111318",
            bordercolor="#1e2230",
            borderwidth=1,
            font=dict(color="#c8d0e0", family="Space Mono", size=11),
            title=dict(text="Type", font=dict(color="#e8f040")),
        ),
        geo=dict(
            bgcolor="#0a0c10",
            landcolor="#1a1f2e",
            oceancolor="#0d1117",
            showocean=True,
            lakecolor="#0d1117",
            showlakes=True,
            countrycolor="#2a3040",
            countrywidth=0.5,
            coastlinecolor="#2a3040",
            coastlinewidth=0.5,
            showframe=False,
        ),
    )

    return fig.to_html(full_html=False, include_plotlyjs='cdn', div_id="map-container", config={"responsive": True})


@app.route('/')
def index():
    disasters = get_disasters()
    stats     = get_stats()
    map_html  = build_map(disasters)
    return render_template('index.html', map_html=map_html, stats=stats, disasters=disasters[:50])


@app.route('/fetch')
def fetch_route():
    """Pobiera dane z NASA i NOAA, zapisuje do bazy, wraca na stronę główną."""
    all_disasters = []

    try:
        nasa_raw = fetch_data(nasa.urls, nasa.params, nasa.items_holder)
        for batch in nasa_raw:
            items = batch if isinstance(batch, list) else [batch]
            all_disasters.extend(convert(items))
    except Exception as e:
        print(f"[NASA] Błąd: {e}")

    try:
        noaa_raw = fetch_data(noaa.urls, noaa.params, noaa.items_holder)
        for batch in noaa_raw:
            items = batch if isinstance(batch, list) else [batch]
            all_disasters.extend(convert(items))
    except Exception as e:
        print(f"[NOAA] Błąd: {e}")

    inserted = save_disasters(all_disasters)
    print(f"[FETCH] Pobrano {len(all_disasters)}, zapisano {inserted} nowych.")
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)