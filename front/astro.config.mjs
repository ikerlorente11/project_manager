// @ts-check
import { defineConfig } from 'astro/config';
import viteConfig from './vite.config.js'; // Importar configuración de Vite

const isDemo = process.env.ENV === 'demo';
const baseUrl = process.env.PUBLIC_BASE_URL || '';

// https://astro.build/config
export default defineConfig({
    base: isDemo ? `${baseUrl}/` : '/',
    output: 'server', // Esto activa SSR
    server: {
        host: true,
        port: 4321,
    },
    vite: viteConfig, // Forzar Astro a usar esta configuración de Vite
});
