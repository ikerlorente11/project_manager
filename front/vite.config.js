import { defineConfig } from 'vite';

const isDemo = process.env.ENV === 'demo';
const baseUrl = process.env.PUBLIC_BASE_URL || '';

export default defineConfig({
    server: {
        host: true,
        port: 4321, // Debe coincidir con el de Astro y Docker
        strictPort: true,
        allowedHosts: ["serveriker.ddns.net"], // Permitir este host específico
    }
});