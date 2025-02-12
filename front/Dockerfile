# Usa una imagen base de Node.js
FROM node:23-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia todos los archivos del proyecto al contenedor
COPY . .

# Expón el puerto en el que la app va a correr
EXPOSE 3000

# Ejecutar startup
CMD ["sh", "/app/startup.sh"]
