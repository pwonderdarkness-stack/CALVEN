import threading
import os
import sys
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.webview import WebView
from kivy.clock import Clock
from kivy.logger import Logger

# Agregar el directorio actual al path para importar app.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def start_flask():
    """Inicia el servidor Flask en un hilo secundario."""
    from app import app
    # Cambiar el puerto si es necesario (evitar conflictos)
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

class BCVWebView(WebView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Esperar un poco a que el servidor esté listo
        Clock.schedule_once(self.load_local_url, 2)

    def load_local_url(self, dt):
        # Cargar la URL local del servidor Flask
        self.url = "http://127.0.0.1:5000"
        Logger.info("BCVApp: Cargando interfaz desde el servidor local")

def main():
    # Arrancar el servidor Flask en segundo plano
    thread = threading.Thread(target=start_flask, daemon=True)
    thread.start()
    Logger.info("BCVApp: Servidor Flask iniciado en segundo plano")
    
    # Mostrar el WebView
    runTouchApp(BCVWebView())

if __name__ == "__main__":
    main()