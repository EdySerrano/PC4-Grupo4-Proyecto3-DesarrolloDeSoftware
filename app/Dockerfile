FROM python:3.12-slim

# Crear un usuario no root para una ejecucion segura
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Evita instalar paquetes innecesarios en la imagen final
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo
COPY app.py ./

# Exponer el puerto de la aplicacion
EXPOSE 5000

# Ejecutar como usuario no root
USER appuser

# Ejecutamos con gunicorn para entorno de produccion ligero
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "-w", "2"]
