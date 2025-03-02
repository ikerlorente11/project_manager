# Use a base image of Node.js
FROM node:23-alpine

# Definir el directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias
COPY package.json package-lock.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto de Angular en desarrollo
EXPOSE 4200

# Comando para ejecutar Angular en desarrollo
CMD ["ng", "serve"]