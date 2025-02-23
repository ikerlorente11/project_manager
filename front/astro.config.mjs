import { defineConfig, envField } from 'astro/config';
import node from '@astrojs/node';

const base = process.env.BASE_URL;

export default defineConfig({
    base: base,
    adapter: node({ mode: 'standalone' }), 
    env: {
        schema: {
            ENV: envField.string({ context: 'server', access: 'public' }),
            BASE_URL: envField.string({ context: 'server', access: 'public', optional: true }),
            SERVER_API_BASE_URL: envField.string({ context: 'server', access: 'public' }),
            PUBLIC_API_BASE_URL: envField.string({ context: 'server', access: 'public' }),
        },
    }
});
