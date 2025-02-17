# Usa la imagen base de Python
FROM python:3.9-alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia los archivos necesarios al contenedor
COPY . .

# Expón el puerto 8000
EXPOSE 8000

# Usar el script de espera antes de levantar la API
CMD ["sh", "/app/wait-for-db.sh"]