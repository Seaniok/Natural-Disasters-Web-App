# 🌍 Natural Disaster Tracker

An interactive web dashboard that visualizes global natural disasters in real-time. This application fetches geological and climate data from professional sources like NASA and NOAA to display them on a dynamic world map.

## 🚀 Features
- **Real-time Monitoring:** Tracks current wildfires, volcanic eruptions, and storms.
- **Interactive Visualizations:** High-quality maps built with Plotly for exploring event locations.
- **Clean Architecture:** Utilizes Python Classes and Inheritance for structured disaster management.
- **Web Interface:** Powered by Flask to serve the dashboard in any browser.

## 🛠️ Tech Stack
- **Python** (Core Logic & OOP)
- **Flask** (Web Framework)
- **Plotly** (Data Visualization)
- **Requests** (API Integration)
- **HTML/CSS** (Frontend Layout)

## 📂 Project Structure
- `app.py` - The main Flask server and web routing.
- `main.py` - Core logic for fetching API data and processing objects.
- `natural_disaster.py` - Data models using OOP classes (`Volcano`, `Wildfire`, `Storm`).
- `templates/index.html` - The frontend dashboard template.

## ⚙️ How to Run
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/natural-disaster-tracker.git](https://github.com/your-username/natural-disaster-tracker.git)
   
   cd natural-disaster-tracker
2. **Install Dependencies:**
    ```bash
    pip install flask requests plotly
3. **Launch the Server:**
    ```bash
    python app.py
4. **Access the dashboard:**
    ```bash
    Open your browser and navigate to http://127.0.0.1:5000