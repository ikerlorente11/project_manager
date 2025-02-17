// @ts-check
import { defineConfig } from 'astro/config';
import viteConfig from './vite.config.js'; // Importar configuración de Vite

// https://astro.build/config
export default defineConfig({
    output: 'server', // Esto activa SSR
    server: {
        host: true,
        port: 4321,
    },
    vite: viteConfig, // Forzar Astro a usar esta configuración de Vite
});
