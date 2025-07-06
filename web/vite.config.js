import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';
import vue from '@vitejs/plugin-vue';
import fg from 'fast-glob';

export default defineConfig({
    plugins: [
        vue(),
        laravel({
            input: [
                'resources/css/app.css',
                'resources/js/app.js',
                'resources/ts/app.ts',
                ...fg.sync('resources/ts/pages/**/*.ts'),
            ],
            refresh: true,
        }),
    ],
});
