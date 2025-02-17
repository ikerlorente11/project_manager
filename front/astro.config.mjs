// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
    server: {
        host: true, // Permite acceso desde cualquier IP
        port: 4321, // Asegúrate de que coincida con el puerto expuesto en Docker
        allowedHosts: ["serveriker.ddns.net"], // Permitir acceso desde este dominio
    }
});