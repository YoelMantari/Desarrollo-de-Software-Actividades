# Imagen con base en python
FROM python:3.9-slim

# Carpeta dentro del contenedor 
WORKDIR /app

# archivo de requerimientos
COPY requirements.txt .

# intalar librerias del app
RUN pip install --no-cache-dir -r requirements.txt

# copiar el proyecto al contenedor
COPY . .

# iniciar el contenedor y arranca el servidor en el puerto 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
