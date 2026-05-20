# Usa una imagen base de Python
FROM python:3.10-slim

# Instala Chrome y las dependencias del sistema que necesita Selenium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Establece la variable de entorno para que Chrome sepa dónde está
ENV CHROME_BIN=/usr/bin/chromium

WORKDIR /app

# Copia e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Comando para iniciar tu aplicación con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]