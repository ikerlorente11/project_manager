import { defineConfig } from 'vite';

export default defineConfig({
    server: {
        host: true,
        port: 4321, // Debe coincidir con el de Astro y Docker
        strictPort: true,
        allowedHosts: ["serveriker.ddns.net"], // Permitir este host específico
    }
});