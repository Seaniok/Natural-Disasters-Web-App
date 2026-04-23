from flask import Flask, render_template
import plotly.express as px 
from modules.natural_disaster import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")