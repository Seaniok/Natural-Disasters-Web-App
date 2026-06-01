from flask import Flask, render_template, jsonify, request
from modules.database import init_db, save_disasters, get_disasters, get_stats
from modules.fetch_data import fetch_data, convert
import modules.nasa_api as nasa
import modules.noaa_api as noaa
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')
 
 
@app.route('/api/disasters')
def api_disasters():
    """Zwraca zdarzenia z bazy jako JSON (opcjonalny filtr ?type=Earthquake)."""
    type_filter = request.args.get('type', None)
    disasters = get_disasters(type_filter=type_filter)
    return jsonify(disasters)
 
 
@app.route('/api/stats')
def api_stats():
    """Zwraca statystyki z bazy."""
    return jsonify(get_stats())
 
 
@app.route('/api/fetch', methods=['POST'])
def api_fetch():
    """
    Ręczne odświeżenie danych z NASA i NOAA.
    Wywołaj POST /api/fetch żeby zaciągnąć nowe dane.
    """
    all_disasters = []
 
    # NASA (wildfires)
    try:
        nasa_raw = fetch_data(nasa.urls, nasa.params, nasa.items_holder)
        for batch in nasa_raw:
            all_disasters.extend(convert(batch if isinstance(batch, list) else [batch]))
    except Exception as e:
        print(f"[NASA] Błąd: {e}")
 
    # NOAA (tsunamis, earthquakes, volcanoes)
    try:
        noaa_raw = fetch_data(noaa.urls, noaa.params, noaa.items_holder)
        for batch in noaa_raw:
            all_disasters.extend(convert(batch if isinstance(batch, list) else [batch]))
    except Exception as e:
        print(f"[NOAA] Błąd: {e}")
 
    inserted = save_disasters(all_disasters)
    return jsonify({
        "fetched": len(all_disasters),
        "inserted": inserted,
        "message": f"Pobrano {len(all_disasters)} zdarzeń, zapisano {inserted} nowych."
    })
 
 
if __name__ == '__main__':
    init_db()
    app.run(debug=True)