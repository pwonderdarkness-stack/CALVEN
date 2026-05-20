from flask import Flask, jsonify
from flask_cors import CORS
from scraper_bcv import BCVClient
import time
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ... (resto del código igual, con la función extraer_valor_moneda y obtener_tasas_bcv)