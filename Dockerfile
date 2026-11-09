# 1. Imagen base: un Linux pequeño que ya trae Python instalado
FROM python:3.12-slim

# 2. Carpeta de trabajo dentro del contenedor (se crea sola)
WORKDIR /app

# 3. Copiamos primero solo requirements.txt e instalamos las librerías.
#    Se hace por separado para que Docker reutilice esta capa
#    y no reinstale todo cada vez que cambies main.py.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos el código de la API al contenedor
COPY main.py .

# 5. Documentamos que la API escucha en el puerto 8000
EXPOSE 8000

# 6. Comando que se ejecuta al arrancar el contenedor.
#    --host 0.0.0.0 es imprescindible: si no, la API solo sería
#    accesible desde dentro del contenedor y no desde tu PC.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]