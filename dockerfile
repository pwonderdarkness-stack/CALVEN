FROM python:3.10-slim

# Instala Chrome, dependencias del sistema y utilidades para depurar
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Variable de entorno para que Chrome sepa dónde está
ENV CHROME_BIN=/usr/bin/chromium

WORKDIR /app

# Copia e instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto que Render espera
EXPOSE 10000

# Comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]